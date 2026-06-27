import os
import hashlib
import time
import urllib.request

PARTIES = {
    "bjp": "Logo_of_the_Bharatiya_Janata_Party.svg",
    "inc": "Indian_National_Congress_hand_symbol.svg",
    "cpim": "Election_Symbol_CPI(M).svg",
    "tmc": "All_India_Trinamool_Congress_symbol.svg",
    "sp": "Samajwadi_Party_Bicycle.svg",
    "bsp": "Elephant_Bahujan_Samaj_Party.svg",
    "tdp": "Telugu_Desam_Party_Election_Symbol.svg",
    "jdu": "Janata_Dal_(United)_Election_Symbol.svg",
    "rjd": "Rashtriya_Janata_Dal_Election_Symbol.svg",
    "shivsena": "Shiv_Sena_Election_Symbol.svg",
    "ysrcp": "Yuvajana_Sramika_Rythu_Congress_Party_Election_Symbol.svg",
    "aiadmk": "All_India_Anna_Dravida_Munnetra_Kazhagam_Election_Symbol.svg",
    "dmk": "Dravida_Munnetra_Kazhagam_Election_Symbol.svg"
}

output_dir = "react-ui/public/symbols"
os.makedirs(output_dir, exist_ok=True)

# Wikimedia requires a clear User-Agent with contact info to prevent 429 rate limit blocks
headers = {
    "User-Agent": "PoliticalPartySim/1.0 (contact: admin@politicalsimgame.com; developer: supratikde)"
}

for key, filename in PARTIES.items():
    # Calculate MD5 hash to locate path
    md5 = hashlib.md5(filename.encode('utf-8')).hexdigest()
    d1 = md5[0]
    d2 = md5[:2]
    
    # 320px is a standard thumbnail size on Wikimedia Commons
    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{d1}/{d2}/{filename}/320px-{filename}.png"
    dest = os.path.join(output_dir, f"{key}.png")
    
    print(f"Downloading {key} -> {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())
        print(f"✅ Successfully saved {key}.png")
    except Exception as e:
        print(f"❌ Failed to download {key} ({filename}): {e}")
        # Try raw SVG if thumbnail fails
        svg_url = f"https://upload.wikimedia.org/wikipedia/commons/{d1}/{d2}/{filename}"
        svg_dest = os.path.join(output_dir, f"{key}.svg")
        print(f"  Attempting raw SVG: {svg_url}...")
        try:
            req_svg = urllib.request.Request(svg_url, headers=headers)
            with urllib.request.urlopen(req_svg) as response, open(svg_dest, 'wb') as out_file:
                out_file.write(response.read())
            print(f"  ✅ Successfully saved {key}.svg as fallback")
        except Exception as svg_err:
            print(f"  ❌ Raw SVG also failed: {svg_err}")
            
    # Throttling to respect Wikimedia's API terms
    time.sleep(1.5)

print("Done checking all downloads.")
