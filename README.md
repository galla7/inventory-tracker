# 📦 Inventory Tracker - CI/CD + Ansible

## ✅ Tech Stack
- Python + Flask app
- GitHub Actions CI/CD
- Ansible for configuration

## 🔧 GitHub Actions
- CI workflow: installs deps, runs tests, uploads artifact
- CD-Test: deploys on main push
- CD-Prod: deploys on manual trigger

## 🔐 Secrets Used
- `TEST_API_KEY` and `PROD_API_KEY` added via Settings > Secrets

## ⚙️ Configuration Management
- Ansible installed via Homebrew
- Configures Python, Flask, and runs app

## 📦 Artifacts
- Tests uploaded using `upload-artifact`

## 🎯 Conclusion
This project automates an inventory app pipeline using real CI/CD and config tools.
