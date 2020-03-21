#RENAME APP
import string
import os
valid_chars = string.ascii_letters + string.digits + '_'

def appName():
    app_name = input('Enter your new app name : ')
    while( (app_name[0].isdigit()) or (False in [c in valid_chars for c in app_name]) ):
        error_message = f'\nApp name must not begin with a digit or contain characters other that letters,digits and underscores:\nEnter your new app name again:'
        app_name = input(error_message)
    return app_name

project_name = input('Enter current project name : ')
current_app_name = input('Enter current app name : ')
app_name = appName()
os.chdir(project_name)

# SETTINGS.PY
with open(f"{project_name}/settings.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            settings_app_name = f"    '{app_name}',\n"
            new_lines.append(settings_app_name)
        else:
            new_lines.append(line)

    with open(f"{project_name}/settings.py",'w') as f:
        for l in new_lines:
            f.write(l)

# URLS.PY
with open(f"{project_name}/urls.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            url_line = line.replace(current_app_name,app_name)
            new_lines.append(url_line)
        else:
            new_lines.append(line)

    with open(f"{project_name}/urls.py",'w') as f:
        for l in new_lines:
            f.write(l)

os.rename(current_app_name, app_name)
os.chdir(app_name)

# VIEWS.PY
with open('views.py','r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            index_app_name = f"    return render(request, '{app_name}/index.html')\n"
            new_lines.append(index_app_name)
        else:
            new_lines.append(line)

    with open('views.py','w') as f:
        for l in new_lines:
            f.write(l)

# APPS.PY
with open('apps.py','r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            apps_name = f"    name = '{app_name}'\n"
            new_lines.append(apps_name)
        else:
            new_lines.append(line)

    with open('apps.py','w') as f:
        for l in new_lines:
            f.write(l)

os.chdir('static')
os.rename(current_app_name, app_name)
os.chdir('../')

os.chdir('templates')
os.rename(current_app_name, app_name)
os.chdir(app_name)

# BASE.HTML
with open('base.html','r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            base_line = line.replace(current_app_name,app_name)
            new_lines.append(base_line)
        else:
            new_lines.append(line)

    with open('base.html','w') as f:
        for l in new_lines:
            f.write(l)

# INDEX.HTML
with open('index.html','r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            index_line = line.replace(current_app_name,app_name)
            new_lines.append(index_line)
        else:
            new_lines.append(line)

    with open('index.html','w') as f:
        for l in new_lines:
            f.write(l)
