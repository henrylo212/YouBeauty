import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youbeauty.settings')

if len(sys.argv) == 1:
    sys.argv.append('runserver')
    sys.argv.append('127.0.0.1:8000')  

sys.argv.append('--noreload')

execute_from_command_line(sys.argv)