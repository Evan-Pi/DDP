import string
import os


valid_chars = string.ascii_letters + string.digits + '_'

#RENAME PROJECT
def ProjectName():
    project_name = input('Enter your new project name : ')
    while( (project_name[0].isdigit()) or (False in [c in valid_chars for c in project_name]) ):
        error_message = f'\nProject name must not begin with a digit or contain characters other that letters,digits and underscores:\nEnter your new project name again:'
        project_name = input(error_message)
    return project_name

current_project_name = input('Enter current project name : ')
project_name = ProjectName()

os.rename(current_project_name, project_name)
os.chdir(project_name)


# MANAGE.PY
with open("manage.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if 'os.environ.setdefault' in line:
            setdefault = f"    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')\n"
            new_lines.append(setdefault)
        else:
            new_lines.append(line)

    with open("manage.py",'w') as f:
        for l in new_lines:
            f.write(l)

# WSGI.PY
with open(f"{current_project_name}/wsgi.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if 'os.environ.setdefault' in line:
            setdefault = f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')\n"
            new_lines.append(setdefault)
        elif 'WSGI config for' in line:
            wsgi_for = f'WSGI config for {project_name} project.\n'
            new_lines.append(wsgi_for)
        else:
            new_lines.append(line)

    with open(f"{current_project_name}/wsgi.py",'w') as f:
        for l in new_lines:
            f.write(l)


# ASGI.PY
with open(f"{current_project_name}/asgi.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if 'os.environ.setdefault' in line:
            setdefault = f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')\n"
            new_lines.append(setdefault)
        elif 'ASGI config for' in line:
            wsgi_for = f'ASGI config for {project_name} project.\n'
            new_lines.append(wsgi_for)
        else:
            new_lines.append(line)

    with open(f"{current_project_name}/asgi.py",'w') as f:
        for l in new_lines:
            f.write(l)

# SETTINGS.PY
with open(f"{current_project_name}/settings.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if 'Django settings for' in line:
            settings_for = f"Django settings for {project_name} project.\n"
            new_lines.append(settings_for)
        elif 'ROOT_URLCONF =' in line:
            root_urlconf = f"ROOT_URLCONF = '{project_name}.urls'\n"
            new_lines.append(root_urlconf)
        elif 'WSGI_APPLICATION =' in line:
            wsgi_application = f"WSGI_APPLICATION = '{project_name}.wsgi.application'\n"
            new_lines.append(wsgi_application)
        else:
            new_lines.append(line)

    with open(f"{current_project_name}/settings.py",'w') as f:
        for l in new_lines:
            f.write(l)

#URLS.PY
with open(f"{current_project_name}/urls.py",'r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if 'URL Configuration' in line:
            url_configuation = f'\"\"\"{project_name} URL Configuration\n'
            new_lines.append(url_configuation)
        else:
            new_lines.append(line)

    with open(f"{current_project_name}/urls.py",'w') as f:
        for l in new_lines:
            f.write(l)

os.rename(current_project_name, project_name)
