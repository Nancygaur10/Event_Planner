Event Planner
📌 Overview

This project is a role-based authentication system built with Django, featuring login, signup, and dashboards for users and admins.

⚙️ Setup and Installation

Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


Run database migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser (optional, for admin access)

python manage.py createsuperuser


Start the development server

python manage.py runserver


Open your browser at:

http://127.0.0.1:8000/

🛠️ Technologies Used

Django – Backend framework chosen for its robust authentication system, ORM, and scalability.

SQLite – Database for managing users and roles. SQLite for development.

HTML, CSS, Bootstrap – For responsive front-end design.

Python – Core programming language for rapid development and clean syntax.

📊 ER Diagram
+-------------------+        +-------------------+
|     CustomUser    |        |       Role        |
+-------------------+        +-------------------+
| id (PK)           | 1    * | id (PK)           |
| username          | <------| name              |
| email             |        |                   |
| password          |        |                   |
| role_id (FK)      |        |                   |
+-------------------+        +-------------------+

File Structure

Event_Planner/                  # Root project folder
├─ manage.py                    # Django project management script
├─ requirements.txt             # Python dependencies
├─ venv/                        # Virtual environment (gitignored)
├─ db.sqlite3                   # SQLite database (gitignored)
├─ Event_Planner/               # Main project folder
│  ├─ __init__.py
│  ├─ settings.py               # Django settings
│  ├─ urls.py                   # Root URL configuration
│  ├─ asgi.py
│  └─ wsgi.py
├─ accounts/                     # App for user/authentication
│  ├─ migrations/
│  │  └─ __init__.py
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py                  # Signup/Login forms
│  ├─ models.py                 # CustomUser & Role models
│  ├─ tests.py
│  └─ views.py                  # Views for signup, login, dashboards
├─ templates/                    # HTML templates
│  ├─ base.html                  # Base template
│  ├─ login.html
│  ├─ signup.html
│  ├─ admin_dashboard.html
│  └─ user_dashboard.html
├─ static/                       # Static files (CSS, JS, images)
│  ├─ css/
│  │  └─ style.css
│  ├─ js/
│  └─ images/
├─ .gitignore
└─ README.md
