# LibraryProject

This project is an introductory setup aimed at familiarizing you with the fundamentals of Django, including environment setup, project creation, and an overview of the default project structure.

## Objective

The primary goal of this project is to gain hands-on experience with Django by:

- Setting up a Django development environment.
- Creating a basic Django project.
- Understanding the default structure of a Django project.

## Prerequisites

- Python installed on your system (version 3.6 or higher recommended).
- pip, the Python package installer, is also required.
- A virtual environment tool, such as `venv` or `virtualenv`, is recommended to manage dependencies.

## Getting Started

Follow these steps to set up your Django development environment and create the LibraryProject:

### Step 1: Set Up a Virtual Environment

1. Open your terminal.
2. Navigate to the directory where you want to create your project.
3. Run the following command to create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```

### Step 2: Install Django

With your virtual environment activated, install Django using pip:

```bash
pip install django
```

### Step 3: Create a New Django Project

1. Run the following command to create a new Django project named LibraryProject:
   ```bash
   django-admin startproject LibraryProject
   ```
2. Navigate into the newly created `LibraryProject` directory:
   ```bash
   cd LibraryProject
   ```

### Step 4: Run the Development Server

1. Start the Django development server to ensure everything is set up correctly:
   ```bash
   python manage.py runserver
   ```
2. Open your web browser and visit `http://127.0.0.1:8000/` to see the default Django welcome page.

## Project Structure Overview

The default structure of a Django project includes the following components:

- **LibraryProject/**: The main project directory containing:
  - **manage.py**: A command-line utility for interacting with the project.
  - **LibraryProject/** (inner folder): The actual project code, containing:
    - ****init**.py**: Indicates that this directory should be treated as a Python package.
    - **settings.py**: Contains settings and configuration for the project.
    - **urls.py**: Defines the URL patterns for the project.
    - **wsgi.py**: An entry point for WSGI-compatible web servers to serve your project.
    - **asgi.py**: An entry point for ASGI-compatible web servers to serve your project asynchronously.

## Next Steps

After setting up your project, you can start building Django applications, define models, and create views to render data to users.
