# Django E-commerce Project - Setup Guide

This is a full-featured E-commerce platform built with Django. Follow the steps below to set up and run the project on a new device.

## Prerequisites
- **Python 3.10+** installed on the system.
- **pip** (Python package manager).

## Setup Instructions

### 1. Extract the Project
Unzip the `Ecommerce.zip` folder to your desired location (e.g., `Desktop`).

### 2. Install Dependencies
Open a terminal (PowerShell or Command Prompt) in the project folder and run:
```bash
pip install -r requirements.txt
```

### 3. Initialize the Database
Run the following commands to set up the database and create the tables:
```bash
    python manage.py migrate
```

### 4. Populate Demo Data (Optional)
To quickly add categories, products, and a superuser (Admin), run:
```bash
python populate_db.py
```

### 5. Run the Server
Start the development server:
```bash
python manage.py runserver
```

## Accessing the Project
- **Main Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard**: [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
- **Django Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Admin Credentials
- **Username**: `admin`
- **Password**: `admin123`

---
*Developed as part of the Django E-commerce Project Synopsis.*
