# Political Party Sim

Prototype for a card-based political strategy game inspired by fictional Indian state elections.

## Sprint 1 Scope

- Spring Boot backend.
- MongoDB persistence for game sessions.
- Create game endpoint.
- Turn-view endpoint.
- Simple Streamlit Python UI for testing party health and public mood.

## Backend

```bash
cd backend
mvn spring-boot:run
```

By default the backend expects MongoDB at:

```text
mongodb://localhost:27017/political_sim
```

You can also create a local env file:

```bash
cp backend/.env.example backend/.env
```

Then update `backend/.env` with your MongoDB connection string.

Override with:

```bash
MONGODB_URI=mongodb://host:port/db mvn spring-boot:run
```

## Python UI

```bash
cd python-ui
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The UI expects the backend at `http://localhost:7810`.

Override with:

```bash
POLITICAL_SIM_API_URL=http://localhost:7810 streamlit run app.py
```

The Streamlit app has two modes:

- `Game`: create/load a game and view current party health.
- `Admin`: maintain scenarios, cards, news, reaction options, rules, and weights in MongoDB.

Game setup supports three parties. Controller mix must be either `1 Human + 2 Computer` or `2 Human + 1 Computer`.
