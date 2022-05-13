# Queue manager MV VISA card
##### Follow these steps to install

1. Install python
2. Create venv in source root: <code>python -m venv venv </code>
3. Activate venv: <code>.\venv\Scripts\activate</code>
4. Install requirements: <code>python install -r requirements.txt</code>
5. <code>cd mvcard</code>
6. Create superuser: <code>python manage.py createsuperuser</code>
7. Migrate db: <code>python manage.py migrate</code>
8. Run server: <code>python manage.py runserver</code>
9. Congrats!