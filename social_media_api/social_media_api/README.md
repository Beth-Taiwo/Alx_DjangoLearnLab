# social_media_api

This project is a social media API built with Django and Django REST Framework. It features user authentication, profile management, and user interactions such as following other users.

### Setup

1. Open your terminal.
2. Navigate to the directory where you want to create your project.

   ```bash
   cd Documents
   django-admin startproject social_media_api
   cd social_media_api
   ```

3. create accounts app

   ```bash
   python3 manage.py startapp accounts
   ```

4. Activate a virtual environment:

   ```bash
   pip install pipenv
   pipenv shell
   ```

5. With your virtual environment created, install Django & djangorestframework using pip:

   ```bash
   pip install django djangorestframework
   ```

6. Creating Models
   in the accounts/models file create a custom user model

   ###### CustomUser

   The `CustomUser` model extends Django's built-in `AbstractUser` model. It includes additional fields for user bio, profile picture, and followers.

   ###### Fields

   - `bio`: A text field for the user's bio. This field is optional.
   - `profile_picture`: An image field for the user's profile picture. Images are uploaded to the `profile_pictures/` directory. This field is optional.
   - `followers`: A many-to-many field representing the users following this user. This field is not symmetrical, meaning that if User A follows User B, User B does not automatically follow User A. The related name for the reverse relation is `following`.

   ###### String Representation

   The string representation of the `CustomUser` model returns the username's profile.

   ```python
   def __str__(self):
       return f"{self.username}'s Profile"
   ```

7. Apply the migrations:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

8. Run the Development Server

   1. Start the Django development server to ensure everything is set up correctly:

      ```bash
      python manage.py runserver
      ```

   2. Open your web browser and visit `http://127.0.0.1:8000/` to see the default Django welcome page.

## Project Structure Overview

The default structure of a Django project includes the following components:

- **social_media_api/**: The main project directory containing:
  - **accounts**: The application directory
    - **migrations**: The migrations directory that contains the migrated models
    - \***\*init**.py\*\*: Indicates that this directory should be treated as a Python package.
    - **admin.py**: The admin file that contains the admin configuration
    - **models.py**: Defines the models for the application.
    - **urls.py**: Defines the URL patterns for the application.
    - **views.py**: Defines the class or function responsible for processing a user's request and for returning response.
  - **manage.py**: A command-line utility for interacting with the project.
  - **social_media_api/** (inner folder): The actual project code, containing:
    - \***\*init**.py\*\*: Indicates that this directory should be treated as a Python package.
    - **settings.py**: Contains settings and configuration for the project.
    - **urls.py**: Defines the URL patterns for the project.
    - **wsgi.py**: An entry point for WSGI-compatible web servers to serve your project.
    - **asgi.py**: An entry point for ASGI-compatible web servers to serve your project asynchronously.
