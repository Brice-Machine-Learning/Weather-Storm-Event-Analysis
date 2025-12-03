# 🧭 Contributing to Storm Events Analysis

Thank you for your interest in contributing!  
This project follows a clean, reproducible ML pipeline and a well-structured development workflow.

## 📚 Related Community Files

This project follows GitHub’s recommended community standards.
Please review the following before contributing:

- **CODE_OF_CONDUCT.md** — expected behavior and reporting guidelines  
- **CONTRIBUTING.md** — development workflow and rules  
- **.github/CODEOWNERS** — automatic reviewer assignment  
- **.github/PULL_REQUEST_TEMPLATE.md** — required PR structure  
- **.github/ISSUE_TEMPLATE/** — issue reporting templates  
- **SECURITY.md** — how to report vulnerabilities  
- **.github/FUNDING.yml** — sponsorship options

---

## 📁 Project Structure Overview
```
storm-events-analysis/
│
├── data/
├── notebooks/
├── reports/
├── models/
├── src/
└── tests/
```

---

## 🛠 Development Environment
Two environments are used:

### **1. Runtime environment**
```
conda env create -f environment.yml
conda activate weather_storm_events_predict
```

### **2. CI environment**
Used only in GitHub Actions:
```
environment_gh_actions.yml
```

---

## 🚦 Code Standards
We use **Ruff** for linting:
```
pip install ruff
ruff check src --fix
```

---

## 🧪 Testing
```
pip install pytest pytest-cov
pytest -v
```

Add tests under `tests/` for any new utilities.

---

## 📝 Notebook Guidelines
- Follow sequential numbering  
- Use relative paths  
- Avoid committing outputs  
- Support the `SAMPLE_RUN` flag for CI

---

## 🔀 Pull Requests
Before submitting a PR:
- Run ruff  
- Run pytest  
- Update docs if needed  
- Follow the PR template

---

## 📄 Commit Style
Use conventional commit prefixes:
```
feat:, fix:, docs:, ci:, refactor:, test:
```

---

## 📫 Contact
- Email: brice@devbybrice.com  
- LinkedIn: https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/  
- Website: https://www.devbybrice.com
