import sys
import os

# Add your project directory to the sys.path
project_home = '/home/your_username/SHALL-Bot'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the PYTHONPATH to include your project directory
os.environ['PYTHONPATH'] = project_home

# Start your bot
import tg_bot

if __name__ == "__main__":
    tg_bot.main()
