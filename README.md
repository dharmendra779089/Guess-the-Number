# Flask Higher-Lower Guessing Game 🎮

A simple, interactive web-based guessing game built using **Python** and **Flask**. The application generates a random number between 0 and 9, and the user tries to guess it by modifying the website's URL path. The application uses dynamic routing to evaluate the user's guess and responds with styled HTML headers and fun, reactive GIFs.



---

## 🚀 Features

* **Dynamic URL Routing:** Captures user input directly from the browser's address bar.
* **Conditional UI Styling:** Color-coded feedback depending on the guess (Purple for *Too High*, Red for *Too Low*, Green for *Winner*).
* **Rich Media Integration:** Animated GIFs loaded via Giphy to make the feedback engaging.
* **Flask Development Mode:** Configured with `debug=True` for instant reloading during local development.

---

## 🛠️ Installation & Setup

Follow these steps to get the project running locally on your machine.

### Prerequisites
Make sure you have **Python 3.x** installed.

### 1. Clone the Repository
```bash
git clone https://github.com/dharmendra779089/Guess-the-Number.git
cd Guess-the-Number
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
python main.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`. Try guessing by appending a number to the URL (e.g. `http://127.0.0.1:5000/5`).

---

## 🌐 Deploying to Render

This project includes a `render.yaml` Blueprint configuration for easy deployment on Render.

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Add production configs for Render"
   git push origin main
   ```
2. **Connect to Render**:
   - Log in to [Render Dashboard](https://dashboard.render.com/).
   - Click **New +** -> **Web Service** (or **Blueprints**).
   - Connect your GitHub repository `dharmendra779089/Guess-the-Number`.
3. **Configuration Settings**:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn main:app`
4. Click **Deploy Web Service**.
