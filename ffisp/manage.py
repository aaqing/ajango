#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
from globals import globals
if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ffisp.settings")
	try:
		globals.set(a='aa')
		globals.set(b='b')
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			"Couldn't import Django. Are you sure it's installed and "
			"available on your PYTHONPATH environment variable? Did you "
			"forget to activate a virtual environment?"
		) from exc
	execute_from_command_line(sys.argv)
