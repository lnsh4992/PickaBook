#!/usr/bin/env python
import os


def run():
    
    print("runManage called!")
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickabook.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


#    ["runManage.py", "runserver"]
    execute_from_command_line(["runManage.py", "runserver"])
