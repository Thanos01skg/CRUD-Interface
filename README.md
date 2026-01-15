<div align="center">

  <h1>🌡️ Django CRUD Interface: Factory Environmental Monitor</h1>
  
  <p>
    <b>A Web-based System for Managing Temperature & Humidity Data.</b>
  </p>

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge" />
  <img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge" />
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code Badge" />

  <br />
  <br />
</div>

---

## 📝 Project Overview

This project is an educational implementation of a **CRUD (Create, Read, Update, Delete)** interface developed using **Django** and **Visual Studio Code**.

The system provides a user-friendly and efficient way to manage environmental data. It allows users to store, view, update, and delete measurements for **Temperature (°C)** and **Humidity (%)**, ensuring full control over the dataset.

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| **Create** | Manually add new measurements via a dedicated input form. |
| **Read** | View a structured table of all recorded data including IDs and values. |
| **Update** | Modify existing records directly from the main dashboard. |
| **Delete** | Remove obsolete or incorrect data entries. |

---

## 🛠️ Tech Stack & Tools

* **Frameworks:** Django, Django REST Framework.
* **Language:** Python.
* **Database:** SQLite (Default Django DB).
* **IDE:** Visual Studio Code.
* **VS Code Extensions:** Python, Python Debugger, Django, SQLite, Prettier, Pylance, Code Runner, open in browser.

---

## 📸 Interface Screenshots

### 1. Main Dashboard
The central hub displaying the table of measurements (`Id`, `Temperature`, `Humidity`) and action buttons.

<img width="550" height="310" alt="crud 1" src="https://github.com/user-attachments/assets/2f177501-db86-41a3-96f0-756d21190d90" />


### 2. Add Measurement Form
The input interface for submitting new environmental data.

<img width="314" height="230" alt="crud 2" src="https://github.com/user-attachments/assets/fc9f8984-65ed-4fc4-9e2a-e0e153892508" />


---

## ⚙️ Installation & Setup Guide

Follow these steps to set up the project locally, as documented in the development process.

### 1. Environment Setup
Ensure you have Python installed. It is recommended to select the correct **Interpreter** or create a **Virtual Environment** via the VS Code Command Palette (`Ctrl + Shift + P` -> `Python: Select Interpreter`).

### 2. Install Dependencies
Open your terminal and install the required frameworks:
```bash
pip install django djangorestframework
```

### 3. Initialize Database
Apply the migrations to set up the SQLite database structure.
* `makemigrations` creates the blueprint for model changes.
* `migrate` applies these changes to the database.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Application
Start the local development server to launch the web interface:
```bash
python manage.py runserver
```
Once running, open your browser and navigate to the local address (usually `http://127.0.0.1:8000/`) to access the CRUD interface.

---

## 📂 Project Structure
The project follows the standard Django architecture:
* `django_project/`: Contains core settings, URLs, and WSGI/ASGI configurations.
* `django_app/`: Contains the main logic including views, models, admin, and tests.
* `db.sqlite3`: The database file storing your measurements.
