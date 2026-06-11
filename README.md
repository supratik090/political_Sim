# Indian Politics Strategy Simulation

A premium, card-based political strategy game inspired by fictional state campaign dynamics in India. Manage resources, form coalitions, draft tactics, bid for mystery rewards, respond to breaking news, and steer policy issues to win government office.

---

## 🎮 Game Architecture & Mechanics

### 1. Gameplay Steps (Turn Wizard)
Each turn represents 1 month in a 60-month election cycle. Players navigate a multi-step stepper board to submit their choices:
1. **Choose Card**: Draft a campaign move from your deck (e.g., Agitation, Scandal, Positive Service, or Governance).
2. **Target Party**: Select which rival party your card targets (if required by card logic).
3. **Play Reward (Optional)**: Play an active booster reward card from your inventory (e.g., Grassroots Boost, Smear Campaign).
4. **News Reactions**: Formulate responses to breaking local news stories. Correct reactions boost support; incorrect ones lead to voter backlash.
5. **Monthly Issue**: Decide on a policy challenge (e.g., agricultural distress, urban infrastructure). Your options heavily sway voter demographics.
6. **Review & Lock**: Double-check your choices, enter your currency bid for the monthly cycle, and lock your turn to advance the round.

### 2. 5-Turn Bidding & Mystery Rewards
* Every turn, parties place blind bids using metrics (Coins, Morale, or Public Support).
* Bidding winners are crowned (`👑`) inline on the last turn decisions panel.
* On Turn 5 of each cycle, the winner of the cumulative bidding rounds is awarded a **Mystery Reward** placed in their inventory (`🎒 Held Rewards`), which can be played in future turns.

### 3. Campaign Era Locks & Progression
* **Start Era (2001)**: Only **West Bengal** is unlocked initially.
* **Locked campaigns** (Maharashtra, Uttar Pradesh, Tamil Nadu, Rajasthan) unlock for play once the human player forms the government (wins) in West Bengal.
* **Era 2006 Unlock**: Winning all 5 campaigns in the 2001 Era progresses the simulation to the **2006 Era**, unlocking advanced campaign scenarios for all five states.

---

## 🛠️ Installation & Setup

### Prerequisites
* **Java**: JDK 17 or higher
* **Database**: MongoDB (running locally or a cloud URI)
* **Python**: Python 3.10 or higher
* **Maven**: For building the backend

---

### 1. Run the Spring Boot Backend

The backend is built with Spring Boot and uses MongoDB for session persistence.

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Set up your environment variables. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
   Modify `.env` to configure your MongoDB connection string:
   ```env
   MONGODB_URI=mongodb://localhost:27017/political_sim
   ```
3. Run the Spring Boot application using Maven:
   ```bash
   mvn spring-boot:run
   ```
   The server starts up by default on port `7810`.

---

### 2. Run the Streamlit Frontend

The frontend is a clean Python dashboard built with Streamlit.

1. Navigate to the python-ui directory:
   ```bash
   cd python-ui
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the frontend server:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501/` in your browser.

---

## 🔑 Authentication & User Scoping

The application isolates active saved games and campaign progression tables per user. Users must log in before accessing campaigns.

### 1. Real Google Authentication
To authenticate users via their real Google accounts, you must create a Web Client ID in the Google Cloud Console.

#### Google Cloud Setup:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Select or create a project, then navigate to **APIs & Services > Credentials**.
3. Create an **OAuth Client ID** for a **Web application**.
4. Set **Authorized JavaScript origins** to:
   `http://localhost:8501` (Do not add trailing slash).
5. Set **Authorized redirect URIs** to:
   `http://localhost:8501/` (Must include trailing slash).
6. Copy the generated **Client ID** and **Client Secret**.

#### Configure Environment:
Set the variables in your terminal before launching Streamlit:
```bash
export GOOGLE_CLIENT_ID="your-client-id.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="your-client-secret"
export GOOGLE_REDIRECT_URI="http://localhost:8501/"
```

### 2. Developer Bypass Login
If you do not have Google credentials configured, you can log in locally via the **Developer Bypass Login** form. Just type any email (e.g., `player@example.com`) and click **Proceed with Mock User**.
* Email addresses are case-insensitive and stripped of whitespace to ensure seamless cross-device loading.

---

## 🛠️ Admin Console

You can access the rule-building interface by clicking the **🛠️ Admin Console** button on the start screen, or by typing:
```text
http://localhost:8501/admin
```
The Admin Console allows you to edit:
* Scenarios (defining starting roles, coins, morale, and starting stats)
* Action Cards (costs, risks, effects)
* News Events & Reaction weights
* Monthly Governance Issues
