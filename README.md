<div align="center">

  <h1>🌡️ Django CRUD Interface: Factory Environmental Monitor</h1>
  
  <p>
    <b>A Web-based System for Managing Temperature & Humidity Data.</b>
  </p>

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge" />
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge" />
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code Badge" />
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML Badge" />
  <img src="https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white" alt="CSS Badge" />

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
The central hub displaying the table of measurements (`Id`, `Temperature`, `Humidity` and `Action buttons`).

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
pip install django
pip install django djangorestframework
```

Verify the installation by checking the Django version:
```bash
django-admin --version
```

### 3. Create the Project
Initialize the main Django project structure named (`django_project`).
```bash
django-admin startproject django_project
```

### 4. Create the Application
Navigate into the project directory and create a new app named (`django_app`) to handle the core functionality.
```bash
cd .\django_project\
django-admin startapp django_app
```

### 5. Initialize Database
Apply the migrations to set up the SQLite database structure.
* `makemigrations` creates the blueprint for model changes.
* `migrate` applies these changes to the database.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Application
Start the local development server to launch the web interface:
```bash
python manage.py runserver
```
Once running, open your browser and navigate to the local address (usually `http://127.0.0.1:8000/`) to access the CRUD interface.

---

## 🎨 Frontend & Project Structure

The user interface is built using standard Django templates and static files to ensure a responsive and user-friendly experience.

### 📂 `templates/` (HTML Views)
This folder contains the HTML files that define the structure of the web pages:
* **`index.html`**: The main dashboard that displays a table of all recorded temperature and humidity measurements.
* **`add.html`**: A form interface that allows users to manually input new environmental data into the system.
* **`update.html`**: A dedicated page for modifying existing records, ensuring data accuracy.

### 📂 `static/` (Styling)
This folder holds the static assets used to style the application:
* **`style.css`**: Contains the custom CSS rules that define the visual layout, colors, and typography, giving the interface a clean and professional industrial look.

---


## 📂 Project Structure
The project follows the standard Django architecture:
* `django_project/`: Contains core settings, URLs, and WSGI/ASGI configurations.
* `django_app/`: Contains the main logic including views, models, admin, and tests.
* `db.sqlite3`: The database file storing your measurements.

---
&nbsp;

## 🗄️ Database Management (SQLite)

The system uses **SQLite** to provide a lightweight and efficient way of storing environmental data. Through **Visual Studio Code**, we can explore, edit, and analyze the database directly within the workspace environment.

### 🔍 SQLite Explorer in VS Code
By utilizing the SQLite extension in VS Code, we gain access to powerful tools:

* **Database Exploration**: Opening `.sqlite3` or `.db` files to view the full structure of the tables.
* **SQL Queries**: Writing and executing SQL queries to filter or update data.
* **Data Interaction**: Easy insertion, editing, or deletion of records.

### 📊 Data Structure: The Measurement Table
The core of this project is the `django_app_measurement` table. This table is automatically generated by the Django model to store data from sensors via the **Raspberry Pi 5** device.

| Column | Description |
| :--- | :--- |
| **id** | The unique identification code for each record. |
| **Temperature** | Ambient temperature values in degrees Celsius. |
| **Humidity** | Relative humidity percentages. |


<img width="214" height="330" alt="crud 2" src="https://github.com/user-attachments/assets/43f573b7-c53a-4477-af23-45eccb5ed919" />
<img width="214" height="330" alt="crud 2" src="https://github.com/user-attachments/assets/c19b306a-dd32-44ea-908e-83c21c842440" />


> [!NOTE]
> The data displayed in the SQLite Explorer is the same as that appearing in the web browser through the CRUD Interface.

### 🛠️ How to View the Database in VS Code
1. Open the **Command Palette** (`Ctrl + Shift + P`).
2. Type and select **"SQLite: Open Database"**.
3. Select the `db.sqlite3` file from your project folder.
4. Expand the **SQLite Explorer** in the bottom-left sidebar to view the `django_app_measurement` table.

### 📈 Practical Application
This structured data allows for:

* **Real-Time Monitoring**: Detecting deviations in temperature or humidity that could affect an industrial environment.
* **Data Visualization**: Data can be displayed in graphs, providing critical information for identifying problems.
* **Decision Making**: Providing a reliable basis for automation and effective real-time decision making.
