import os
from PIL import Image

# Set your root directory here
root_dir = "./images/characters"

for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(foldername, filename)
            png_path = os.path.join(foldername, f"{os.path.splitext(filename)[0]}.png")

            try:
                with Image.open(webp_path) as img:
                    img.save(png_path, "PNG")
                # Delete the original .webp file
                os.remove(webp_path)
                print(f"Converted and deleted: {webp_path} -> {png_path}")
            except Exception as e:
                print(f"Failed to convert {webp_path}: {e}")