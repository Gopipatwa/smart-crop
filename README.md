# Smart Crop

Smart Crop is a Python tool to automatically detect, crop, and extract stickers or avatars (including attached signs like bulbs, zzz, question marks, etc.) from an image. It removes the background from each detected sticker and saves all results in a single zip file for easy sharing or use.

## Features
- Detects and crops all stickers/avatars from an image, including attached signs.
- Removes background from each cropped sticker using rembg.
- Saves all cropped stickers as PNGs in a zip file named after the input image.
- Cleans up by deleting the individual sticker images after zipping.

## Requirements
- Python 3.7+
- See `requirements.txt` for dependencies:
  - pillow
  - rembg
  - onnxruntime
  - opencv-python

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/smart-crop.git
   cd smart-crop
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Place your input image in the `images/` folder (or provide the path).
2. Run the script:
   ```sh
   python main.py images/your_image.jpg
   ```
3. The cropped stickers will be saved as PNGs and zipped in the `cropped_emojis/` folder. Only the zip file will remain after processing.

## Output
- All cropped stickers are saved in a zip file named after your input image (e.g., `your_image.zip`).
- The zip file is located in the `cropped_emojis/` folder.

## License
MIT License
