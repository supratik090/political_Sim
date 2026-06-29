# Indian Politics Strategy Simulation

A premium, card-based political strategy simulation inspired by state-level campaign dynamics in India. Manage resources, draft campaign tactics, respond to news cycles, fund projects, and survive political crises to win government office.

🔗 **Live Demo**: The hosted game is available at [https://political-sim-mu.vercel.app](https://political-sim-mu.vercel.app) for review.

For a detailed explanation of the gameplay mechanics, backend architecture, and AI decision-making algorithms, see **[walkthrough.md](walkthrough.md)**.

---

## 🛠️ Prerequisites
*   **Java**: JDK 17 or higher
*   **Maven**: For building and running the Spring Boot backend
*   **Database**: MongoDB (local connection or a cloud MongoDB Atlas instance)
*   **NodeJS / npm**: For building and running the production React UI frontend

---

## 🚀 Step-by-Step Run Guide

### Step 1: Configure & Start Spring Boot Backend
1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Copy `.env.example` to `.env` and set variables:
    ```bash
    cp .env.example .env
    ```
3.  Edit the `.env` file and set your `MONGODB_URI` (remote MongoDB Atlas or local connection):
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

### Step 2: Run the Frontend

Choose one of the frontend clients below to start:

#### Option A: React UI (Web)
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

#### Option B: Flutter UI (Web, Desktop, Mobile)
1.  Navigate to the `flutter-ui` directory:
    ```bash
    cd flutter-ui
    ```
2.  Fetch packages and dependencies:
    ```bash
    flutter pub get
    ```
3.  Run the application on Chrome (Web):
    ```bash
    flutter run -d chrome --web-port 5174
    ```
    Or run on local emulators (Android/iOS) or native desktop targets by launching:
    ```bash
    flutter run
    ```

---

## 🔑 Authentication
The game uses email-and-password credentials to isolate and persist campaign sessions per user. Simply register an account or log in with your credentials on the start screen.

---

## 🛠️ Admin Console
You can access the rule-building dashboard to create or edit cards, news items, and scenarios:
*   Select the **Admin Console** link in the navigation menu on the React UI.


