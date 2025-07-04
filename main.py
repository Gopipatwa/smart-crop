from PIL import Image
from rembg import remove
import os
import cv2
import sys
import zipfile

def detect_and_crop_stickers(input_path, output_folder):
    img_cv = cv2.imread(input_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    # Threshold to get binary image (tune threshold as needed)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    pil_img = Image.open(input_path)
    os.makedirs(output_folder, exist_ok=True)
    idx = 1
    img_w, img_h = pil_img.size
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Filter out very small regions (noise)
        if w < 30 or h < 30:
            continue
        # Expand bounding box by 10% only for width
        margin_w = int(w * 0.2)
        x1 = max(x - margin_w, 0)
        y1 = y
        x2 = min(x + w + margin_w, img_w)
        y2 = y + h
        cropped = pil_img.crop((x1, y1, x2, y2))
        cropped_rgba = cropped.convert("RGBA")
        output = remove(cropped_rgba)
        output_path = os.path.join(output_folder, f"f2_{idx}.png")
        output.save(output_path, format="PNG")
        print(f"Saved {output_path}")
        idx += 1

    # After saving all stickers, create a zip file
    base_img_name = os.path.splitext(os.path.basename(input_path))[0]
    zip_path = os.path.join(output_folder, f"{base_img_name}.zip")
    sticker_files = []
    for i in range(1, idx):
        sticker_file = os.path.join(output_folder, f"f2_{i}.png")
        if os.path.exists(sticker_file):
            sticker_files.append(sticker_file)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for sticker_file in sticker_files:
            zipf.write(sticker_file, os.path.basename(sticker_file))
    print(f"Created zip: {zip_path}")
    # Delete all sticker images after zipping
    for sticker_file in sticker_files:
        os.remove(sticker_file)
    print("Deleted all sticker images after zipping.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_folder = "cropped_emojis"
    detect_and_crop_stickers(input_path, output_folder)