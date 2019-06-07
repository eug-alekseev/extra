Simple python-flask application with mysql connection. 
Has been made for testing purposes and does not bring any value.

```
information about connection to database and application IP and port is taken primarily from environment variables and secondly from config.py
requirements.txt contains list of python modules to be installed
tested on python 3.7.2
```
Environment variables:
```
EXTRAAPP_MYSQL_USER : mysql username
EXTRAAPP_MYSQL_PASS : mysql password
EXTRAAPP_MYSQL_HOST : mysql hostname
EXTRAAPP_MYSQL_DB   : mysql database name
EXTRAAPP_DEBUG_MODE : debug mode
EXTRAAPP_PORT       : application port
EXTRAAPP_IP         : application IP
```
Parameters to run:
```python3 app.py```
