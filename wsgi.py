import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/SHALL-Bot'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Activate your virtual environment
activate_this = os.path.expanduser('~/.virtualenvs/yourenv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set the PYTHONPATH to include your project directory
os.environ['PYTHONPATH'] = project_home

# Import and start your bot
import tg_bot

if __name__ == "__main__":
    from tg_bot import updater
    updater.start_polling()
