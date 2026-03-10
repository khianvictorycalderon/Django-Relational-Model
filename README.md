# Django Relational Model
An experimental project with Django models that are relational. I used [Apixer](https://apixer.vercel.app) to test the APIs of this project.

## Setup
1. Clone this repository via `git clone https://github.com/khianvictorycalderon/Django-Relational-Model.git`
2. Generate a safe key using this command in your python interpreter or cmd:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
3. Create an `.env` file that contains (paste the generated key in `DJANGO_SECRET_KEY`):
    ```env
    DJANGO_ENV=development
    DJANGO_SECRET_KEY=your-key-here
    DEBUG=True
    ```
4. Go to `django_relational_model/settings.py` and look for the `Allowed Origins` part and update it depending on your frontend or API tester.
    Change the allowed and trusted credentials depending on where you want your project to be tested.
5. Run the following command for database migration:
    - `python manage.py makemigrations` or `py manage.py makemigrations`
    - `python manage.py migrate` or `py manage.py migrate`
6. To run the server, run `py manage.py runserver` or `python manage.py runserver`
    NOTE: If you encounter `Error: You don't have permission to access that port.`, just use a different port, for example:
    - `py manage.py runserver 8001`
    - `python manage.py runserver 8002`
    8001 and 8002 are the port.
7. To create another app, just run `python manage.py startapp <app-name>` or `py manage.py startapp <app-name>`, example: `py manage.py startapp myapp`

## Admin
1. To access the database using admin panel type in the url: "/admin"
2. Run `py manage.py createsuperuser` then enter the email, username, and password you want to use
3. You can edit your database now by logging in your account

## Prerequisites:
Install the following first (globally) if you haven't installed it yet:
- `pip install django`
- `pip install djangorestframework`
- `pip install django-cors-headers`