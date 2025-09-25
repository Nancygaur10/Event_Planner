# Event Planner - Role-Based Authentication System

## 📍 Overview

This project is a **role-based authentication system** built with **Django**, featuring login, signup, and dashboards for users and admins. Users have roles assigned to them, and access is restricted based on these roles.

---

## 🔧 Setup and Installation

### 1. Clone the Repository

```
git clone https://github.com/Nancygaur10/Event_Planner.git
cd Event_Planner
```

### 2. Create and Activate Virtual Environment

```
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Access)

```
python manage.py createsuperuser
```

### 6. Start the Development Server

```
python manage.py runserver
```

### 7. Open in Browser

Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ Technologies Used

* **Django** – Backend framework for authentication, ORM, and scalability.
* **SQLite / PostgreSQL** – Database for managing users and roles (SQLite for development, PostgreSQL recommended for production).
* **HTML, CSS, Bootstrap** – Frontend for responsive UI.
* **Python** – Core programming language for clean and rapid development.

---

## 📁 Project File Structure

```
Event_Planner/
├─ manage.py
├─ requirements.txt
├─ venv/                    # Virtual environment (gitignored)
├─ db.sqlite3               # Database (gitignored)
├─ Event_Planner/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ accounts/
│  ├─ migrations/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ templates/
│  ├─ base.html
│  ├─ login.html
│  ├─ signup.html
│  ├─ admin_dashboard.html
│  └─ user_dashboard.html
├─ static/
│  ├─ css/
│  ├─ js/
│  └─ images/
├─ .gitignore
└─ README.md
```

---

## 📊 ER Diagram

```
+-------------------+        +-------------------+
|     CustomUser    |        |       Role        |
+-------------------+        +-------------------+
| id (PK)           | 1    * | id (PK)           |
| username          | <------| name              |
| email             |        |                   |
| password          |        |                   |
| role_id (FK)      |        |                   |
+-------------------+        +-------------------+
```

---

## 📍 Notes

* Make sure to **activate the virtual environment** before running server commands.
* `.gitignore` excludes virtual environment and database files.
* You can switch to **PostgreSQL** for production by updating `settings.py`.
