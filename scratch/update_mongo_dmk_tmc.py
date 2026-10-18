import json
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.political_sim

with open('seed-data/national/national_configs/2001.json', 'r') as f:
    cfg_data = json.load(f)

# Find existing 2001 config in mongo
existing = db.national_configs.find_one({"era": 2001})
if existing:
    cfg_data["_id"] = existing["_id"]
    if "id" in existing:
        cfg_data["id"] = existing["id"]
    db.national_configs.replace_one({"_id": existing["_id"]}, cfg_data)
    print("Updated existing national_configs for era 2001 in MongoDB.")
else:
    db.national_configs.insert_one(cfg_data)
    print("Inserted national_configs for era 2001 in MongoDB.")

# Also update existing active/archived games if needed or print info
print("TMC and DMK are now NDA in 2001 config.")
