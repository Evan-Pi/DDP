import string
import subprocess
import shutil
import os

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++RENAME PROJECT ↓
current_project_name = input('Enter current project name : ')

# Validate project name through django back end ↓
project_name = input('Enter new project name:')
cmd = f'django-admin startproject {project_name}'
returned_value = subprocess.call(cmd, shell=True)

while returned_value == 1:
    project_name = input('Enter new project name again:')
    cmd = f'django-admin startproject {project_name}'
    returned_value = subprocess.call(cmd, shell=True)
else:
    print('Project name accepted')

shutil.rmtree(project_name)
# Validate project name through django back end ↑

os.rename(current_project_name, project_name)
os.chdir(project_name)

# MODIFY MANAGE.PY
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

# MODIFY WSGI.PY
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


# MODIFY ASGI.PY
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

# MODIFY SETTINGS.PY
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++RENAME PROJECT ↑

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++RENAME APP ↓
current_app_name = input('Enter current app name : ')
# Validate app name through django back end ↓
app_name = input('Enter new app name:')
cmd = f'python manage.py startapp {app_name}'
returned_value = subprocess.call(cmd, shell=True)

while returned_value == 1:
    app_name = input('Enter new app name again:')
    cmd = f'python manage.py startapp {app_name}'
    returned_value = subprocess.call(cmd, shell=True)
else:
    print('App name accepted')

shutil.rmtree(app_name)
# Validate app name through django back end ↑

# MODIFY SETTINGS.PY
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

# MODIFY URLS.PY
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

# MODIFY VIEWS.PY
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

# MODIFY APPS.PY
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

# MODIFY BASE.HTML
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

# MODIFY INDEX.HTML
with open('index.html','r') as f:
    lines = f.readlines()
    new_lines = []
    for line in lines:
        if current_app_name in line:
            index_line = line.replace(current_app_name,app_name)
            new_lines.append(index_line)
        elif current_project_name in line:
            index_project_name_line = line.replace(current_project_name,project_name)
            new_lines.append(index_project_name_line)
        else:
            new_lines.append(line)

    with open('index.html','w') as f:
        for l in new_lines:
            f.write(l)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++RENAME APP ↑
