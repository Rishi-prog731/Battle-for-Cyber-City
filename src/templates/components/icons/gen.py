import os

# get icons

icon_path = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..', '..', '..', 'static', 'img', 'icons'))
print(icon_path)

icons = []
for root, dirs, files in os.walk(icon_path):
    for file in files:
        icons.append(file)

print(icons)

# create templates
for icon in icons:
    print(os.path.join(os.path.dirname(__file__), icon[:-4] + '.html.jinja'))
    with open(os.path.join(os.path.dirname(__file__), icon[:-4] + '.html.jinja'), 'w') as f:
        f.write('<img class="icon" src="{{ url_for(\'static\', filename=\'img/icons/' + icon + '\') }}" alt="' + icon[:-4] + '" />')