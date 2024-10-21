# Fitness Tracker API

## 📋 Project Overview
The **Fitness Tracker API** is a Django-based backend system that enables users to track fitness activities, manage their accounts, and view activity summaries.

## 🛠️ Features
- **Activity Management**: Create, Read, Update, and Delete (CRUD) operations for fitness activities.
- **User Authentication**: JWT-based authentication for secure access.
- **Activity Metrics**: Provides total duration, calories burned, etc., with filters.
- **Pagination & Sorting**: Paginate and sort activities by various criteria.

## 🔧 Technologies Used
- **Django**: Backend framework.
- **Django REST Framework (DRF)**: API development.
- **SQLite**: Default database.

## 🚀 Getting Started

### Prerequisites
- Python 3.12.7
- Django & DRF
- Virtual environment

### 🚀Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/MMSleem/fitness-tracker-api-project.git
   cd fitness-tracker-api-project
   
2. **Set up a virtual environment**:

Run python -m venv env to create the environment.
Activate it using source env/bin/activate (For Windows: env\Scripts\activate).
🛠️ Creates an isolated environment for the project dependencies.

3. **Install dependencies**:

Run pip install -r requirements.txt to install necessary packages.
📦 Installs all the project requirements.

4. **Migrate the database**:

Run python manage.py migrate to set up the database schema.
💾 Initializes the database structure.

5. **Create a superuser**:

Run python manage.py createsuperuser to add an admin account.
🔑 Allows access to the Django admin interface.

6. **Run the development server**:

Start the server using python manage.py runserver.
🚀 Starts the project on your local machine.


## 📖 API Endpoints
### Authentication
Login: /api/token/ (POST)
Refresh Token: /api/token/refresh/ (POST)

### Users
-Create User: /api/users/ (POST)
-Get User: /api/users/<id>/ (GET)
### Activities
-Create Activity: /api/activities/ (POST)
-List Activities: /api/activities/ (GET)
-Update Activity: /api/activities/<id>/ (PUT)
-Delete Activity: /api/activities/<id>/ (DELETE)