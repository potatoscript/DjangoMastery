# Django Potato Project

## A. Create Django Project

Follow the steps below to build the Django project:

### Step-by-Step Instructions

1. **Create a Directory for the Project**
   ```bash
   mkdir django-potato
   ```

2. **Navigate into the Directory and Create a Virtual Environment**
   ```bash
   cd django-potato
   python -m venv potatovm
   ```

3. **Activate the Virtual Environment**
   ```bash
   source potatovm/Scripts/activate  # On Windows
   source potatovm/bin/activate      # On Unix or MacOS
   ```

4. **Install Django**
   ```bash
   pip install django
   ```

5. **Install MySQL Client**
   ```bash
   pip install mysqlclient
   ```

6. **Download and Install MySQL**
   Download MySQL from [MySQL Installer](https://dev.mysql.com/downloads/installer/).

7. **Install MySQL Connector**
   ```bash
   pip install mysql-connector-python
   ```

8. **Create Django Project**
   ```bash
   django-admin startproject potatopj
   ```

9. **Navigate into the Project Directory**
   ```bash
   cd potatopj
   ```

10. **Create an App inside the Project**
    ```bash
    python manage.py startapp potatomenu
    ```

11. **Update `settings.py`**
    - Add the new app to `INSTALLED_APPS`:
      ```python
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'potatomenu',
      ]
      ```

    - Configure the database section to use MySQL:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'potato',
              'USER': 'root',
              'PASSWORD': 'potato',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```

12. **Setup the Database**
    Create a file `createdb.py` in the project directory containing:
    ```python
    import mysql.connector

    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='potato'
    )

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database
    cursorObject.execute("CREATE DATABASE potato")

    print("Database created")
    ```

    Run the following command to create the database:
    ```bash
    python createdb.py
    ```

13. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

14. **Create a Superuser**
    ```bash
    winpty python manage.py createsuperuser  # On Windows using Git Bash
    python manage.py createsuperuser         # On Unix or MacOS
    ```

15. **Run the Server**
    ```bash
    python manage.py runserver
    ```

    If you see the Django start screen, it means everything works and we are good to go.

## B. Version Control

### Set Up Version Control with Git and GitHub

1. **Create an SSH Key on Your Computer**

2. **Configure Git**
    ```bash
    git config --global user.name "potatoscript"
    git config --global user.email "potatoscript@yahoo.com"
    git config --global push.default matching
    git config --global alias.co checkout
    git init
    ```

3. **Add and Commit Files to Git**
    ```bash
    git add .
    git commit -am 'Initial Commit'
    ```

4. **Push to GitHub**
    - Create a repository on GitHub
    - Add the remote repository and push:
      ```bash
      git remote add origin git@github.com:youraccountname/repositoryname.git
      git branch -m main
      git push -u origin main
      ```

## C. Build the App

### Setting Up `urls.py` in Project Directory

1. **Update `urls.py` in `potatopj`**
    ```python
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('potatomenu.urls')),
    ]
    ```

2. **Create `urls.py` in `potatomenu` Directory**
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]
    ```

3. **Update `views.py` in `potatomenu` Directory**
    ```python
    from django.shortcuts import render

    def home(request):
        return render(request, 'home.html', {})
    ```

4. **Create `home.html` Template**
    - Create a `templates` directory in `potatomenu`
    - Create `home.html` inside `templates` directory with the following content:
      ```html
      <h1>Hello Potato!</h1>
      ```

By following these steps, you will have a Django project set up with MySQL as the database, version control configured with Git and GitHub, and a basic application structure ready for further development.
