SETUP THE VIRTUAL ENVIRONMENT
_$ python3 -m venv env
_$ . env/bin/activate

To deactivate
_$ deactivate


HOW TO START AND RUN THE APPLICATION:

1. Start the virtual environment by running the command: source venv/bin/activate
2. Run the application by running the command: flask run --host=0.0.0.0 --debug=True
3. Open the browser and go to the URL: http://localhost:5000/


FACTORY PATTERN FOLDER STRUCTURE
This provides the application to be modualr and
to keep all moudles de-coupled and independant
of any other module.

- gcoms_app
    - app ---------------------------------------------> Contains all the Application Modules
        - auth ----------------------------------------> Module / Package
            - static
                - css
                - js
                - img

            - templates
                auth.html

            auth_models.py
            auth_routes.py
            __init__.py

        - dashboard -----------------------------------> Module / Package
             - static
                - css
                - js
                - img

            - templates
                dashboard.html

            dashboard_models.py
            dashboard_routes.py
            __init__.py

        - regions --------------------------------------> Module / Package
             - static
                - css
                - js
                - img

            - templates --------------------------------> Contains Module's UI Templates
                regions.html

            regions_models.py --------------------------> DB Models | imports routes | imported into app/__init__.py
            regions_routes.py --------------------------> Module's Routes that pertain to regions. Imported into Blueprint
            __init__.py --------------------------------> Module's Blueprint

        __init__.py ------------------------------------> Main entry point for the app. Uses a Factory function to create the app
        - templates
            base.html ----------------------------------> The main layout that all the modules get loaded into.
        - static
        

    - env ----------------------------------------------> Virtual Environment + Conatains all the application dependices
    config.py ------------------------------------------> Contains all app environment variables. Imported into app/__init__.py
    gcoms.db -------------------------------------------> SQLite3 database


FLASK LOGIN MANAGER

In templates use:

{% if user.is_authenticated %}
    do something
{% else %}
    do something else
{% endif %}
