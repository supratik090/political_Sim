import os
from PIL import Image

# Path to the uploaded chart image
img_path = '/Users/supratikde/.gemini/antigravity/brain/1fb961c8-e009-45d2-90c9-b28da02badba/media__1782551541414.png'
output_dir = 'react-ui/public/symbols'
os.makedirs(output_dir, exist_ok=True)

# Pixel-perfect grid divider coordinates from image scanning
cols_x = [86, 167, 249, 328, 411]
rows_y = [45, 125, 212, 310, 386, 463]

# Map (row, col) indices to party keys
SYMBOL_MAP = {
    (0, 0): "inc",
    (0, 1): "bjp",
    (0, 2): "bsp",
    (0, 3): "rjd",
    (1, 1): "cpim",
    (1, 3): "tdp",
    (2, 0): "sp",
    (2, 1): "shivsena",
    (2, 3): "tmc",
    (3, 3): "aiadmk",
    (4, 0): "dmk",
    (4, 3): "jdu"
}

img = Image.open(img_path)

def make_transparent_if_white(cropped_img):
    # Convert to RGBA
    rgba = cropped_img.convert("RGBA")
    datas = rgba.getdata()
    
    new_data = []
    for item in datas:
        # If pixel is very close to white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    rgba.putdata(new_data)
    return rgba

for (r, c), name in SYMBOL_MAP.items():
    x1 = cols_x[c]
    y1 = rows_y[r]
    x2 = cols_x[c+1]
    y2 = rows_y[r+1]
    
    # Subtract exactly 18 pixels from the bottom to crop out the party text labels cleanly
    y2_symbol = y2 - 18
    
    cropped = img.crop((x1, y1, x2, y2_symbol))
    
    # For parties with white background, make them transparent
    if name in ["inc", "rjd", "tdp", "shivsena", "tmc", "aiadmk", "jdu"]:
        processed = make_transparent_if_white(cropped)
    else:
        # Keep original colored backgrounds (BJP, BSP, CPIM, SP, DMK)
        processed = cropped.convert("RGBA")
        
    dest_path = os.path.join(output_dir, f"{name}.png")
    processed.save(dest_path, "PNG")
    print(f"✅ Extracted and saved {name}.png (x: {x1}-{x2}, y: {y1}-{y2_symbol})")

print("All extractions complete!")
