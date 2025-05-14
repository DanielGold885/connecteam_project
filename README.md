# Connecteam Automation Assignment

This is a UI automation project developed as part of a home assignment.  
The goal was to automate job application flow on the [Connecteam Careers page](https://connecteam.com/careers/).

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

## ▶ 3. Run tests and generate Allure results

```bash
pytest --alluredir=allure-results
```


#### Prerequisites:

### Install the Allure report:
💻 For Windows:
Install with Chocolatey:
```bash
choco install allure
```

🐧 For Linux/macOS:
Install with Homebrew (macOS):
```bash
brew install allure
```

### Launch the report to view results post-run:
```bash
allure serve allure-results
```

