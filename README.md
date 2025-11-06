# solar-challenge-week0

How to reproduce the Python environment used for this project.

Prerequisites

- Git
- Python 3.11+ (or 3.x)
- PowerShell or cmd (Windows)

Clone and checkout

```powershell
git clone https://github.com/<your-user>/solar-challenge-week0.git
cd "c:\Users\User\projects\solar-challenge-week0"
git checkout setup-task
```

Create and activate a virtual environment (Windows)
PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verify

```powershell
python --version
python -c "import pandas,numpy; print('pandas', pandas.__version__, 'numpy', numpy.__version__)"
```

If you change dependencies

1. Activate venv.
2. Install new packages: `pip install <pkg>`
3. Update requirements: `pip freeze > requirements.txt`
4. Commit and push.

CI

- Workflow: .github/workflows/ci.yml
- The workflow runs `python --version` and `pip install -r requirements.txt` to reproduce the environment on GitHub runners.

check
