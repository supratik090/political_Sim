# Indian Politics Strategy Simulation

A premium, card-based political strategy game inspired by fictional state campaign dynamics in India. Manage resources, form coalitions, draft tactics, bid for mystery rewards, respond to breaking news, and steer policy issues to win government office.

---

## 🎮 Game Architecture & Mechanics

### 1. Gameplay Steps (Turn Wizard)
Each turn represents 1 month in a 60-month election cycle. Players navigate a structured multi-step wizard to formulate their monthly decisions:
1. **Choose Card**: Draft a campaign strategy card from your deck (e.g., *Agitation*, *Scandal*, *Positive Service*, or *Governance*). Cards cost coins/morale and affect party/public stats.
2. **Target Party**: If the selected card targets another political entity, choose the rival party (e.g., *Tiger Front*, *Peacock Party*) that will receive the effects.
3. **Play Reward (Optional)**: Deploy an active booster reward from your inventory (e.g., *Grassroots Boost*, *Smear Campaign*). Rewards are earned via bidding.
4. **News Reactions**: Review the breaking local news story of the month and select your party's response. A correct reaction increases support, while an incorrect response triggers voter backlash.
5. **Monthly Issue**: Decide on a policy challenge (e.g., agricultural distress, urban infrastructure). Your choices sway demographics and public satisfaction.
6. **Review & Lock**: Double-check your moves for the month, input your coin/morale/support bid for the monthly bidding cycle, and lock your turn to advance the round.

### 2. Bidding & Mystery Rewards
* Each turn, parties place blind bids using their resources (Coins, Morale, or Public Support).
* Turn-by-turn bid winners are shown inline in the decisions panel.
* On Turn 5 of each cycle, the party with the highest cumulative bids wins a **Mystery Reward**.
* Mystery Rewards are stored in your inventory (`🎒 Held Rewards`) and can be played during the *Play Reward* step of subsequent turns.

### 3. Campaign Era Locks & Progression
* **Start Era (2001)**: Only **West Bengal** is unlocked initially.
* **Locked Campaigns**: Maharashtra, Uttar Pradesh, Tamil Nadu, and Rajasthan are locked. They automatically unlock once the player wins the West Bengal campaign (forms the government).
* **Era 2006 Unlock**: Winning all 5 campaigns in the 2001 Era progresses the simulation to the **2006 Era**, unlocking advanced campaign scenarios for all five states.

---

## 🛠️ Step-by-Step Execution Guide

To run the simulation, you need to launch the MongoDB database, run the Spring Boot backend, seed the database with cards/news/issues, and then launch the Streamlit frontend.

### Prerequisites
* **Java**: JDK 17 or higher
* **Database**: MongoDB (running locally or a cloud URI)
* **Python**: Python 3.10 or higher
* **Maven**: For building and running the backend

---

### Step 1: Start MongoDB
Ensure MongoDB is running on your machine.
* **macOS (Homebrew)**:
  ```bash
  brew services start mongodb-community
  ```
* **Direct Terminal Execution**:
  ```bash
  mongod --dbpath /path/to/data/db
  ```
* Ensure it is reachable via your configured URI (default: `mongodb://localhost:27017/political_sim`).

---

### Step 2: Build & Run the Spring Boot Backend

The backend manages game state, runs the turn resolution engine, and stores campaign configurations.

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Configure environment variables. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Edit the `.env` file to set your MongoDB connection URI and server port:
   ```env
   MONGODB_URI=mongodb://localhost:27017/political_sim
   PORT=7810
   ```
4. Start the Spring Boot application using Maven:
   ```bash
   mvn spring-boot:run
   ```
   The server will start up on port `7810`. Scenario definitions (West Bengal, Maharashtra, etc.) are seeded automatically on startup.

---

### Step 3: Seed Game Content (Required)

The database must be seeded with cards, news events, and governance issues. Run these scripts **after** starting the backend:

1. Navigate to the `seed-data` directory:
   ```bash
   cd seed-data
   ```
2. Execute the import scripts using Python (uses standard library components; no external dependencies required):
   ```bash
   # Import standard action cards and news event data
   python3 import_review_content.py
   
   # Import monthly issues and extra funding cards
   python3 import_issue_and_extra_cards.py
   ```
3. Verify that the output shows successful deletions and insertions for cards, news, and issues.

---

### Step 4: Run the Streamlit Frontend

The frontend is a Python-based interactive dashboard.

1. Navigate to the `python-ui` directory:
   ```bash
   cd python-ui
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501/` in your web browser.

---

## 🔑 Authentication & User Scoping

The application isolates active saved games and campaign progression tables per user. Users must log in before accessing campaigns.

### 1. Developer Bypass Login
If you do not have Google credentials configured, you can log in locally via the **Developer Bypass Login** form on the start screen.
* Simply enter your email address (e.g., `player@example.com`) and click **Proceed with Mock User**.
* Email inputs are case-insensitive and trimmed of spaces to ensure smooth syncing across devices.

### 2. Google OAuth 2.0 Integration
To authenticate users via their Google accounts:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Select or create a project, then navigate to **APIs & Services > Credentials**.
3. Create an **OAuth Client ID** for a **Web application**.
4. Configure the origins and redirects:
   * **Authorized JavaScript origins**: `http://localhost:8501` (No trailing slash)
   * **Authorized redirect URIs**: `http://localhost:8501/` (Must include trailing slash)
5. Copy the generated **Client ID** and **Client Secret**.
6. Set the environment variables in your terminal before launching Streamlit:
   ```bash
   export GOOGLE_CLIENT_ID="your-client-id.apps.googleusercontent.com"
   export GOOGLE_CLIENT_SECRET="your-client-secret"
   export GOOGLE_REDIRECT_URI="http://localhost:8501/"
   ```

---

## 🛠️ Admin Console

You can access the rule-building interface by clicking the **🛠️ Admin Console** button on the start screen, or by directly visiting:
```text
http://localhost:8501/admin
```
* **Monthly Governance Issues**: Define policy challenges and demographic outcomes.

---

## 🚀 Deploying the Backend to Railway

Railway provides native support for Spring Boot projects. Follow these steps to deploy the backend service:

### 1. Pre-deployment Verification
* Make sure your latest changes (including any directory reorganizations) are pushed to your GitHub repository.
* The Spring Boot backend dynamically binds to the `$PORT` environment variable via the `server.port: ${PORT:8080}` property configured in `application.yml`. No code changes are needed.

### 2. Create a Railway Service
1. Log in to your [Railway Dashboard](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo**.
3. Select your repository (`political_Sim`).

### 3. Configure Subdirectory (Root Directory)
Because the codebase is structured as a monorepo, you must tell Railway to build the Java code from the `backend` subdirectory:
1. In the Railway dashboard, select the newly created service.
2. Go to the **Settings** tab.
3. Scroll down to the **General** section and locate **Root Directory**.
4. Set the **Root Directory** to `/backend`.
5. Railway will automatically detect the `pom.xml` configuration, build the project with Nixpacks, and deploy it.

### 4. Setup Environment Variables
1. Go to the **Variables** tab of the service.
2. Add your database connection string:
   * **Key**: `MONGODB_URI`
   * **Value**: Your MongoDB Atlas connection string (or reference a Railway MongoDB database instance using `${{MongoDB.MONGODB_URI}}`).
3. Railway automatically injects the `$PORT` variable; you do not need to add it manually.
4. Click **Deploy** to rebuild the application with the new variables.

### 5. Expose the Public URL
1. Go to the **Settings** tab of the service.
2. Under **Networking**, click **Generate Domain** (or set up a custom domain) to expose the service to the internet.
3. Update the frontend's API base URL in your configuration (e.g., in `python-ui/constants.py` or `.env`) to point to your new Railway backend domain.
