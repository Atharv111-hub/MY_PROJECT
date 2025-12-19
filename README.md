# MY_PROJECT

This repository contains a Django workspace with two projects: `myproject` and `office_project`.

Quick start (local):

- Activate your virtual environment (example if venv is `my_project\my_project`):
```powershell
cd C:\Users\LENOVO\Desktop\MY_PROJECT
.\my_project\Scripts\Activate.ps1
```

- Install dependencies and create `requirements.txt` (recommended):
```powershell
python -m pip install -r requirements.txt  # if you already have it
# or generate requirements after installing packages you need
python -m pip freeze > requirements.txt
```

- Run the `office_project` server (example):
```powershell
cd C:\Users\LENOVO\Desktop\MY_PROJECT\office_project
python manage.py migrate --settings=office_project.settings
python manage.py runserver --settings=office_project.settings
```

Pushing to GitHub (example):

```powershell
cd C:\Users\LENOVO\Desktop\MY_PROJECT
git init
git add .
git commit -m "Initial commit"
# create a GitHub repo manually or with `gh` CLI
# then add remote, e.g.:
git remote add origin https://github.com/<your-username>/MY_PROJECT.git
git branch -M main
git push -u origin main
```

CI: A simple GitHub Actions workflow is included to run tests on push.
