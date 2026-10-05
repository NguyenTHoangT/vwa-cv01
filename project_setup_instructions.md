Press Ctrl + Shift + V to open the full preview.
# VWA - cv01 (E-shop API)

This is a basic FastAPI project with a SQLite database for the VWA course.

## 1. First-Time Setup (Installation)
*Run these commands only once when you first create or download the project.*

1. **Create the virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   * **Linux / Mac:** `source venv/bin/activate`
   * **Windows:** `.\venv\Scripts\activate`

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 2. How to Run the Project (Next Time)
*Follow these steps every time you open PyCharm, VS Code, or your terminal to work on the project.*

1. **Open your terminal** inside the project folder.
2. **Check for `(venv)`:** Look at the beginning of your terminal line. If you DO NOT see `(venv)`, you must activate it:
   ```bash
   source venv/bin/activate
   ```
3. **Start the server:**
   Once `(venv)` is active, start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

---

## 3. Testing the API
Once the server is running, open your web browser and go to the interactive Swagger UI to test your endpoints (GET, POST, etc.):
👉 **http://localhost:8000/docs**