import os
import json
import sqlite3

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXPORT_DIR = os.path.join(ROOT_DIR, "seed-data", "exported")
ASSETS_DB_DIR = os.path.join(ROOT_DIR, "react-ui", "android", "app", "src", "main", "assets", "database")
DB_PATH = os.path.join(ASSETS_DB_DIR, "statecraft.db")

os.makedirs(ASSETS_DB_DIR, exist_ok=True)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

print(f"Creating SQLite database at: {DB_PATH}")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. Create tables exactly matching Room's schema
cursor.executescript("""
CREATE TABLE IF NOT EXISTS `users` (`id` TEXT NOT NULL, `name` TEXT NOT NULL, `email` TEXT NOT NULL, `password_hash` TEXT NOT NULL, `secret_question` TEXT NOT NULL, `secret_answer_hash` TEXT NOT NULL, `created_at` INTEGER NOT NULL, PRIMARY KEY(`id`));
CREATE UNIQUE INDEX IF NOT EXISTS `index_users_email` ON `users` (`email`);

CREATE TABLE IF NOT EXISTS `game_sessions` (`id` TEXT NOT NULL, `user_id` TEXT NOT NULL, `scenario_key` TEXT NOT NULL, `status` TEXT NOT NULL, `current_turn` INTEGER NOT NULL, `total_turns` INTEGER NOT NULL, `last_election_winner` TEXT, `data_json` TEXT NOT NULL, `updated_at` INTEGER NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_game_sessions_user_id` ON `game_sessions` (`user_id`);
CREATE INDEX IF NOT EXISTS `index_game_sessions_scenario_key` ON `game_sessions` (`scenario_key`);
CREATE INDEX IF NOT EXISTS `index_game_sessions_status` ON `game_sessions` (`status`);

CREATE TABLE IF NOT EXISTS `scenarios` (`scenario_key` TEXT NOT NULL, `name` TEXT NOT NULL, `state_name` TEXT NOT NULL, `start_year` INTEGER NOT NULL, `active` INTEGER NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`scenario_key`));
CREATE INDEX IF NOT EXISTS `index_scenarios_state_name` ON `scenarios` (`state_name`);

CREATE TABLE IF NOT EXISTS `cards` (`id` TEXT NOT NULL, `scenario_key` TEXT NOT NULL, `card_key` TEXT NOT NULL, `name` TEXT NOT NULL, `category` TEXT NOT NULL, `active` INTEGER NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_cards_scenario_key` ON `cards` (`scenario_key`);
CREATE INDEX IF NOT EXISTS `index_cards_card_key` ON `cards` (`card_key`);

CREATE TABLE IF NOT EXISTS `news` (`id` TEXT NOT NULL, `scenario_key` TEXT NOT NULL, `news_key` TEXT NOT NULL, `title` TEXT NOT NULL, `type` TEXT NOT NULL, `active` INTEGER NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_news_scenario_key` ON `news` (`scenario_key`);
CREATE INDEX IF NOT EXISTS `index_news_news_key` ON `news` (`news_key`);

CREATE TABLE IF NOT EXISTS `bills` (`id` TEXT NOT NULL, `scenario_key` TEXT NOT NULL, `bill_key` TEXT NOT NULL, `name` TEXT NOT NULL, `active` INTEGER NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_bills_scenario_key` ON `bills` (`scenario_key`);
CREATE INDEX IF NOT EXISTS `index_bills_bill_key` ON `bills` (`bill_key`);

CREATE TABLE IF NOT EXISTS `factions` (`id` TEXT NOT NULL, `scenario_key` TEXT NOT NULL, `faction_key` TEXT NOT NULL, `name` TEXT NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_factions_scenario_key` ON `factions` (`scenario_key`);
CREATE INDEX IF NOT EXISTS `index_factions_faction_key` ON `factions` (`faction_key`);

CREATE TABLE IF NOT EXISTS `party_management` (`id` TEXT NOT NULL, `game_id` TEXT NOT NULL, `party_id` TEXT NOT NULL, `data_json` TEXT NOT NULL, PRIMARY KEY(`id`));
CREATE INDEX IF NOT EXISTS `index_party_management_game_id` ON `party_management` (`game_id`);

CREATE TABLE IF NOT EXISTS room_master_table (id INTEGER PRIMARY KEY,identity_hash TEXT);
INSERT OR REPLACE INTO room_master_table (id,identity_hash) VALUES(42, 'e4495e49f41a2b0eacc24ef279a8f41a');
""")

def extract_start_year(scenario_key):
    if not scenario_key:
        return 2001
    last4 = scenario_key[-4:]
    return int(last4) if last4.isdigit() else 2001

# 2. Insert Scenarios
scenarios_path = os.path.join(EXPORT_DIR, "scenarios.json")
if os.path.exists(scenarios_path):
    with open(scenarios_path, "r", encoding="utf-8") as f:
        scenarios = json.load(f)
    print(f"Inserting {len(scenarios)} scenarios...")
    for s in scenarios:
        s_key = s.get("scenarioKey") or s.get("id")
        name = s.get("name", "")
        state_name = s.get("stateName", "")
        start_year = extract_start_year(s_key)
        active = 1 if s.get("active", True) else 0
        cursor.execute(
            "INSERT OR REPLACE INTO scenarios (scenario_key, name, state_name, start_year, active, data_json) VALUES (?, ?, ?, ?, ?, ?)",
            (s_key, name, state_name, start_year, active, json.dumps(s))
        )

# 3. Insert Cards
cards_path = os.path.join(EXPORT_DIR, "cards.json")
if os.path.exists(cards_path):
    with open(cards_path, "r", encoding="utf-8") as f:
        cards = json.load(f)
    print(f"Inserting {len(cards)} cards...")
    for c in cards:
        c_id = c.get("id") or str(c.get("_id", ""))
        s_key = c.get("scenarioKey", "")
        c_key = c.get("cardKey", "")
        name = c.get("name", "")
        category = c.get("category", "")
        active = 1 if c.get("active", True) else 0
        cursor.execute(
            "INSERT OR REPLACE INTO cards (id, scenario_key, card_key, name, category, active, data_json) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (c_id, s_key, c_key, name, category, active, json.dumps(c))
        )

# 4. Insert News
news_path = os.path.join(EXPORT_DIR, "news.json")
if os.path.exists(news_path):
    with open(news_path, "r", encoding="utf-8") as f:
        news_items = json.load(f)
    print(f"Inserting {len(news_items)} news items...")
    for n in news_items:
        n_id = n.get("id") or str(n.get("_id", ""))
        s_key = n.get("scenarioKey", "")
        n_key = n.get("newsKey", "")
        title = n.get("title", "")
        n_type = n.get("type", "")
        active = 1 if n.get("active", True) else 0
        cursor.execute(
            "INSERT OR REPLACE INTO news (id, scenario_key, news_key, title, type, active, data_json) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (n_id, s_key, n_key, title, n_type, active, json.dumps(n))
        )

# 5. Insert Bills
bills_path = os.path.join(EXPORT_DIR, "bills.json")
if os.path.exists(bills_path):
    with open(bills_path, "r", encoding="utf-8") as f:
        bills = json.load(f)
    print(f"Inserting {len(bills)} bills...")
    for b in bills:
        b_id = b.get("id") or str(b.get("_id", ""))
        s_key = b.get("scenarioKey", "")
        b_key = b.get("billKey", "")
        name = b.get("name", "")
        active = 1 if b.get("active", True) else 0
        cursor.execute(
            "INSERT OR REPLACE INTO bills (id, scenario_key, bill_key, name, active, data_json) VALUES (?, ?, ?, ?, ?, ?)",
            (b_id, s_key, b_key, name, active, json.dumps(b))
        )

# 6. Insert Factions
factions_path = os.path.join(EXPORT_DIR, "factions.json")
if os.path.exists(factions_path):
    with open(factions_path, "r", encoding="utf-8") as f:
        factions = json.load(f)
    print(f"Inserting {len(factions)} factions...")
    for fa in factions:
        fa_id = fa.get("id") or str(fa.get("_id", ""))
        s_key = fa.get("scenarioKey", "")
        fa_key = fa.get("factionKey", "")
        name = fa.get("name", "")
        cursor.execute(
            "INSERT OR REPLACE INTO factions (id, scenario_key, faction_key, name, data_json) VALUES (?, ?, ?, ?, ?)",
            (fa_id, s_key, fa_key, name, json.dumps(fa))
        )

# 7. Insert Party Management State (seed templates if any)
pm_path = os.path.join(EXPORT_DIR, "party_management.json")
if os.path.exists(pm_path):
    with open(pm_path, "r", encoding="utf-8") as f:
        pm_items = json.load(f)
    print(f"Inserting {len(pm_items)} party management records...")
    for pm in pm_items:
        pm_id = pm.get("id") or str(pm.get("_id", ""))
        game_id = pm.get("gameId", "")
        party_id = pm.get("partyId", "")
        cursor.execute(
            "INSERT OR REPLACE INTO party_management (id, game_id, party_id, data_json) VALUES (?, ?, ?, ?)",
            (pm_id, game_id, party_id, json.dumps(pm))
        )

conn.commit()
cursor.execute("VACUUM")
conn.close()

db_size_mb = os.path.getsize(DB_PATH) / (1024 * 1024)
print(f"SUCCESS! Pre-populated database generated at: {DB_PATH} ({db_size_mb:.2f} MB)")
