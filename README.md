# DDP
Django (3.0.4) Default Project

This repository contains some of the default elements I personally use in every
Django Project. It also contains a python script that gives you the ability
to rename the project as well as the prebuilt app that you will find inside the
project.


Installation instructions:

Clone or download the repository

Create a virtual environment
    virtualenv virtual_environment_name (requires virtualenv library - pip install virtualenv)

Activate the virtual environment
    Windows terminal command : virtual_environment_name\Scripts\activate
    Linux terminal command : source ./virtual_environment_name/bin/activate

Install the dependencies via the requirements.txt file.
    pip install -r requirements.txt

Rename the project as well as the app name by running the rename.py script
    Terminal command : python rename.py (don't forget to navigate to the folder that contains rename.py)

    Important information:
        Current project name : DDP
        Current app name : ddp_app

    Rename steps
        Enter current project name : DDP
        Enter new project name: your_project_name
        Enter current app name : ddp_app
        Enter new app name: your_app_name
