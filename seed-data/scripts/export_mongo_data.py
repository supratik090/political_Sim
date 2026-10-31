import os
import json
import datetime
from bson import ObjectId
import pymongo

MONGO_URI = "mongodb+srv://supratikde090:ztDTTjn5upUs2gai@cluster0.hgdwptz.mongodb.net/political_sim"
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "exported"))

os.makedirs(OUTPUT_DIR, exist_ok=True)

class MongoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return super().default(obj)

def clean_doc(doc):
    if "_id" in doc:
        doc["id"] = str(doc.pop("_id"))
    if "_class" in doc:
        doc.pop("_class")
    return doc

def export_collection(db, collection_name, output_filename):
    print(f"Exporting {collection_name} to {output_filename}...")
    coll = db[collection_name]
    cursor = coll.find()
    docs = [clean_doc(d) for d in cursor]
    out_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, cls=MongoEncoder)
    print(f"  -> Exported {len(docs)} documents to {out_path}")
    return docs

def main():
    print(f"Connecting to MongoDB Atlas...")
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
    db = client.get_default_database()
    
    collections_to_export = [
        ("scenario_definitions", "scenarios.json"),
        ("card_definitions", "cards.json"),
        ("news_definitions", "news.json"),
        ("legislative_bill_definitions", "bills.json"),
        ("faction_definitions", "factions.json"),
        ("party_management_state", "party_management.json"),
    ]
    
    for coll_name, out_file in collections_to_export:
        export_collection(db, coll_name, out_file)
        
    print(f"All collections exported successfully to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
