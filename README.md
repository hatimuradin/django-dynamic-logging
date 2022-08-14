# django-dynamic-logging
Set of tools for handling django logs dynamically instead of static config files

### Handlers
Different Handlers can be defined in `models.HandlerTypes`
Currently two basic handlers defined:
1. console
2. splunk(Socket)

main view is just a hello world but it runs log on all levels.

### Dynamic settings:
1. enable: Boolean to select if all logging available on root logger or not
2. handler: set handler for root logger to be which of handlers

### Demo
after starting server on `manage.py runserver`, navigate to admin and change settings.

default port for splunk is set to `9900`

splunk simulation logs can be seen with `nc -l -u 9900` on linux like machines

