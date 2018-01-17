# Filemanager Python3 Flask Application #

### A Flask sample application for Rich Filemanager ###
This is a functional implementation of Rich Filemanager using Python3 and Flask for the server side connector. This application is intended to be used as an example and not for production. The author is not responsible for any damages that may result from use.

Rich Filemanager is an open-source file manager. See https://github.com/servocoder/RichFilemanager

### Dependencies ###
* Python3
* Flask http://flask.pocoo.org/docs/0.12/
* Pillow (PIL) http://pillow.readthedocs.io/en/latest/
* Virtualenv http://flask.pocoo.org/docs/0.12/installation/#virtualenv

### How do I get set up? ###

This installation differs from the usual Rich Filemanager installation. The application is a stand-alone Flask application and does not use Apache. For integration with Apache see the WSGI version of this app (coming soon).

Flask is setup to load static files, like javascript and css files, from the static folder relative to our Flask file (FlaskApp.py) by default. Because of this Rich Filemanager will be located in the static folder.

If you already have a FLask application setup you will not need FlaskApp.py, just use it as an example. Notice how the blueprint from File.py is loaded. A template is also included so that you can use serve Rich Filemanager's GUI via Flask and implement your own Login and ACL.

### Security ###

For security reasons it is recommended you replace static/RichFilemanager/index.html with an empty index.html if you don't intend to use it. Also you should implement your own user authentication/ authorization system. Authentication and authorization in Flask is well documented and beyond the scope of this documentation.

**It is up to you to manage file system access on your server.** The application should be running with limited file system access.  **DO NOT** run as root or with sudo!

### Installation ###
```bash
source flaskfilemanagerenv/bin/activate
export FLASK_APP=FlaskApp.py
python3 -m flask run
Open your browser and go to http://localhost:5000/files/filemanager
```

### Other Considerations ###

#### Werkzeug Development Server ####
Consider using Flask with a production web server.
From the [Werkzeug](http://werkzeug.pocoo.org/docs/0.14/serving/) site:
> The development server is not intended to be used on production systems. It was designed especially for development purposes and performs poorly under high load. For deployment setups have a look at the [Application Deployment](http://werkzeug.pocoo.org/docs/0.14/deployment/#deployment) pages.

