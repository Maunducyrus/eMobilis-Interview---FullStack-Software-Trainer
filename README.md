python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject school
cd school
python manage.py startapp students


pip install djangorestframework
python manage.py makemigrations
python manage.py migrate


endpoints
http://127.0.0.1:8000/api/students/ - GET
http://127.0.0.1:8000/api/students/1/ GET-ONE
http://127.0.0.1:8000/api/students/ - POST
http://127.0.0.1:8000/api/students/1/ - PUT
http://127.0.0.1:8000/api/students/1/ - DELETE


@api_view decorator - It turns a regular Django function into an API view. It ensures the function can handle specific HTTP methods (like GET or POST)

StudentSerializer - The Serializer acts as a translator.
In GET: It converts database objects into JSON.

In POST/PUT: It takes incoming JSON, validates it (checks if data is correct), and converts it back into a database object.

get_object_or_404 - It's a defensive coding practice. If a user tries to edit a student with an ID that doesn't exist, get() would crash the server with an error.

Response and return render - student_list (API): Returns raw JSON data. This is used for decoupled frontends or mobile apps.

student_ui_list (UI): Returns an HTML template (list.html). This is used for traditional server-side rendered websites

