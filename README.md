# Connecteam Automation Assignment

This is a UI automation project developed as part of a home assignment.  
The goal was to automate job application flow on the [Connecteam Careers page](https://connecteam.com/careers/).

---

## 📌 Project Goal

Automate the following test scenario:

1. Navigate to [https://connecteam.com](https://connecteam.com)
2. Scroll to the footer and click **Careers**
3. Filter positions by **R&D**
4. For each visible R&D position:
   - Click **Apply now**
   - Fill out the application form:
     - First Name
     - Last Name
     - Email
     - Phone
     - CV upload
   - 🚫 Do **not** submit the application (form triggers reCAPTCHA)

---

## 🚀 How to Run

### 🧩 1. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

## 📦 2. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ 3. Run the test

```bash
pytest tests/test_apply_to_rnd.py -v
```
