Wagtail Admin Headless
======================

Open API schemas to define React forms.
 
    Django Channels
    Django Rest Framework
    Open API schemas
    React JSON Schema form       +
    ==============================
    Wagtail admin on steroids


- ✅ Django Rest Framework can expose the model definition in Open API JSON Schemas.
- ✅ React JSON Schema form takes the Open API JSON Schema and renders a form.
- 🚧 API CRUD 
- 🚧 Django Channels + Django Rest Framework for live updates.
- 🚧 ...

Install
-------

    cd frontend
    npm install
    npm run build
    cd ..
    
    create venv
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    127.0.0.1:8000/admin/  # Login to create a session.
    127.0.0.1:8000/  # React form based on model definition.

Demo
----

    CTRL + C
    Add a field to `home.models.HomePage`.
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    reload browser, a field has been added to the React form.


Urls
----

    /admin/  # Wagtail admin
    /openapi/?format=openapi-json  # JSON
    /api/homepages/  # List / Create
    /api/homepages/{id}/  # Detail / Update


Why React and Channels?
-----------------------

- Collaborative editing
- Store React state for partial drafts (required fields can be omitted).
- Undo/redo React state allows undo/redo over all fields.
- ...

To figure out
-------------

There are many unknown. Focus on regular Django models first.

- Alternative for Django custom widgets
- Validation of fields that depend on each other (unique together, etc)  
- Streamfields
- Draft JS
- ...


Django Channels Rest Framework
------------------------------
Django Channels Rest Framework provides a DRF like interface for building channels-v2 websocket consumers.
https://github.com/hishnash/djangochannelsrestframework
https://www.oddbird.net/2018/12/12/channels-and-drf/


Open API schemas
----------------
Django REST Framework provides support for automatic generation of OpenAPI schemas.
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md


React jsonschema-form
--------------------
A simple React component capable of using JSON Schema to build and customize web forms.
https://github.com/rjsf-team/react-jsonschema-form

Demo:
https://rjsf-team.github.io/react-jsonschema-form/

A from is defined via 3 JSON structures:

- JSONSchema  # The form fields.
- UISchema  # The widget and presentation data. A boolean can be a checkbox, select or radio.
- formData  # The data from the endpoint. 
