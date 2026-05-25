import os
import sys

try:
    from PIL import Image, ImageChops
except ImportError:
    print("Pillow not found, installing...")
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image, ImageChops

assets_dir = r"c:\Heronaves STL\assets"

def trim(im):
    # Convert to grayscale
    gray = im.convert("L")
    # Threshold to ignore dark gray/black (e.g. less than 25/255)
    mask = gray.point(lambda p: p > 25 and 255)
    bbox = mask.getbbox()
    if bbox:
        # Provide a little padding just in case, but getbbox is usually tight
        return im.crop(bbox)
    return im

count = 0
for file in os.listdir(assets_dir):
    if "Provas Sociais" in file and file.endswith(".png"):
        path = os.path.join(assets_dir, file)
        try:
            img = Image.open(path)
            cropped = trim(img)
            cropped.save(path)
            print(f"Successfully cropped {file}")
            count += 1
        except Exception as e:
            print(f"Error processing {file}: {e}")

print(f"Finished processing {count} images.")
