# dfb_full_tutorial
https://www.youtube.com/watch?v=sm1mokevMWk
youtube - Django For Beginners - Full Tutorial tech with tim

setup:
pyenv local 3.10.10 - creates python-version file
pyenv virtualenv 3.10.10 dfb_full_tutorial - just first time to create venv
pyenv activate dfb_full_tutorial
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
poetry init - makes pyproject.toml
poetry add django - adds it as a dependency
poetry install - installs the dependencies
poetry run django-admin startproject mysite - creates the django project
dfb_full_tutorial/gitinit
pyenv virtualenv-delete dfb_full_tutorial
pyenv virtualenv 3.10.10 django_notes
pyenv activate django_notes
poetry install
poetry add django-crispy-forms
poetry add crispy-bootstrap5


/mysite$ python manage.py startapp main - create an app
/mysite$ python manage.py startapp register

to start:
/mysite$ python manage.py runserver

database:
python manage.py makemigrations main - create database after creating models
python manage.py migrate - migrate changes
python manage.py shell - python shell, to execute databse commands
>>> from main.models import Item, ToDoList
>>> t = ToDoList(name='todo list')
>>> t.save()
>>> ToDoList.objects.all()
>>> s = ToDoList(name='shopping list')
>>> ToDoList.objects.get(id=1)
>>> ToDoList.objects.get(name='todo list')
>>> t.item_set.all()
>>> t.item_set.create(text='clear pond', complete=False)
>>> t = ToDoList.objects
>>> t.all()
>>> t.filter(id=1)
>>> to_do_list = ToDoList.objects.get(id=1)
>>> to_do_list.item_set.all()
>>> to_do_list.item_set.create(text="apply jobs", complete=True)
>>> richs_list = ToDoList.objects.get(id=2)
>>> richs_list.item_set.all()


{% csrf_token %} - required in all forms
form.as_p - paragraph? there are more _ options

python manage.py createsuperuser - for /admin account richdjaQ223@
python manage.py changepassword <user_name>- if they forget

info:
/home/rich/.pyenv/versions/3.10.10/envs/dfb_full_tutorial/lib/python3.10/site-packages/

Error: That port is already in use.
(django_notes) rich@mx:~/projects/python/django/django_notes/mysite$ lsof -i:8000
kill -9 pid
