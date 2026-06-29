# Indian Politics Strategy Simulation

A premium, card-based political strategy simulation inspired by state-level campaign dynamics in India. Manage resources, draft campaign tactics, respond to news cycles, fund projects, and survive political crises to win government office.

For a detailed explanation of the gameplay mechanics, backend architecture, and AI decision-making algorithms, see **[walkthrough.md](walkthrough.md)**.

---

## 🛠️ Prerequisites
*   **Java**: JDK 17 or higher
*   **Maven**: For building and running the Spring Boot backend
*   **Database**: MongoDB running locally (default: `mongodb://localhost:27017/political_sim`) or a cloud MongoDB Atlas instance
*   **Python**: Python 3.10 or higher (for content seeding scripts)
*   **NodeJS / npm**: For building and running the production React UI frontend

---

## 🚀 Step-by-Step Run Guide

### Step 1: Start MongoDB
Ensure MongoDB is running locally:
*   **macOS (Homebrew)**:
    ```bash
    brew services start mongodb-community
    ```
*   **Direct Execution**:
    ```bash
    mongod --dbpath /path/to/data/db
    ```

---

### Step 2: Configure & Start Spring Boot Backend
1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Copy `.env.example` to `.env` and set variables:
    ```bash
    cp .env.example .env
    ```
3.  Edit the `.env` file:
    ```env
    MONGODB_URI=mongodb://localhost:27017/political_sim
    PORT=7810
    ```
4.  Run the application using Maven:
    ```bash
    mvn spring-boot:run
    ```
    The backend will start on port `7810` and seed scenario definitions automatically on startup.

---

### Step 3: Seed Game Content (Required)
The database must be populated with cards, news stories, and issues before playing. Run these scripts **after** starting the backend:
1.  Navigate to the `seed-data` directory:
    ```bash
    cd seed-data
    ```
2.  Run the import scripts using Python:
    ```bash
    python3 import_review_content.py
    python3 import_issue_and_extra_cards.py
    ```
3.  Verify that the console shows successful imports.

---

### Step 4: Run the Frontends

1.  Navigate to the `react-ui` directory:
    ```bash
    cd react-ui
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the development server:
    ```bash
    npm run dev
    ```
    Open `http://localhost:5173/` in your browser.

---

## 🔑 Authentication
The game isolates active sessions per user:
1.  **Developer Bypass Login**: Enter any mock email address (e.g., `player@example.com`) to bypass Google credentials and log in locally.
2.  **Google OAuth 2.0 Integration**: Set client credentials in the environment before launching React:
    ```bash
    export GOOGLE_CLIENT_ID="your-client-id.apps.googleusercontent.com"
    export GOOGLE_CLIENT_SECRET="your-client-secret"
    export GOOGLE_REDIRECT_URI="http://localhost:5173/"
    ```

---

## 🛠️ Admin Console
You can access the rule-building dashboard to create or edit cards, news items, and scenarios:
*   Select the **Admin Console** link in the navigation menu on the React UI.

---

## 📤 Deploying the Backend to Railway

1.  Log in to [Railway](https://railway.app/).
2.  Create a **New Project** and connect your GitHub repository.
3.  Go to the service's **Settings** tab.
4.  Set the **Root Directory** to `/backend`. Railway will detect `pom.xml` and build using Nixpacks.
5.  In the **Variables** tab, add your remote MongoDB connection string as `MONGODB_URI`.
6.  Generate a domain under **Networking** and update your React configuration files to point to the new domain.
