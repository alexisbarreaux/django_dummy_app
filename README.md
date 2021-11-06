# django_dummy_app

Django dummy app with a postgresql database.

## Virtual environment

### Creating venv

This app was built using a virtual environment initial in the root directory of the project (something like **.../GitHub/django_dummy_app** on your own computer) with

```shell
python -m venv .
```

### Running venv

On windows you then activate the venv with, which might will differ for other settings.

```shell
.\Scripts\Activate.ps1
```

### Path issues

**Note** : I personnaly found out that building virtual environments this way didn't seem to add the current directory to path. So if your current path isn't in your python path, you might thus need to either use an export path before running this and within your activated venv (which isn't very convenient):

```shell
export PYTHONPATH="${PYTHONPATH}:/Users/username/Documents/..... path to repo"
```

Or and according to a [stack overflow issue](https://stackoverflow.com/a/10739838/13736095), if you rather build your venv with the **virutalenv** command, you should be ok with creating a .pth file (with wathever name you want) in the **"/Lib/site-packages"** folder. In this file put the absolute path to your project, in order for python to recognize modules. It is normally done automatically by some venvs (or poetry) but seems to not be the case here and thus we have python raising ModuleNotFoundError when trying to run code.

### Changing IDE interpreter

You will have to change your python interpreter to the one created with the venv,
meaning you'll have to point to something like **C:\Users\my_wonderful_user\Documents\GitHub\django_dummy_app\Scripts\python.exe**.

## Running the app

### Running the server

To run the server, from the root directory do

```shell
python .\inventory_site\manage.py runserver
```

## Postgresql database

### Create database

I used (as you can see in **inventory_site/inventory_site/settings.py**) a database
called inventory with an owner and superuser named inventory_user running on localhost.
The password is also stored in the settings. I didn't have the time to make it secure
or use a .env.
As I ran it locally I'll ask you to also make a local database.

### Make migrations

If you indeed did make a local database you will have to make the needed migrations with

```shell
python .\inventory_site\manage.py migrate
```

### App superuser

My site superuser has the name **admin** (surprising) and password **MYgr8t9GxnQfdUOudCp2** created with

```shell
python .\inventory_site\manage.py createsuperuser
```

## Testing the app

### Building objects

Since I ran on a local database you will have to do the same and thus recreate
objects. With the app running and after having made the database and migrations
go to **http://127.0.0.1:8000/admin**.
There :

-   create a store item
-   create an employee for the store
-   create a product displayed in the store.

### Testing

With the app running, you can go on your localhost and more specifically to
**http://127.0.0.1:8000/inventory** . This will redirect you to a login page,
where you can enter the name of the employee you just created.

Then submitting the form you will be redirected to the display of the names
and expiry dates of the products of the store.

You'll then be able to add or update expiry dates from this page.
