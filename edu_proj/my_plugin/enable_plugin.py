import os

def find_settings_file(start_dir):
    for root, dirs, files in os.walk(start_dir):
        if 'settings.py' in files:
            return os.path.join(root, 'settings.py')
    return None

def modify_settings_file(app_name, settings_file_path):
    with open(settings_file_path, 'r') as f:
        lines = f.readlines()

    # Look for INSTALLED_APPS and append your app's configuration
    for i, line in enumerate(lines):
        if line.startswith('INSTALLED_APPS = ['):
            lines[i] = line.rstrip() + f"\n    '{app_name}',\n"

    with open(settings_file_path, 'w') as f:
        f.write(''.join(lines))

def install():
    app_name = 'pluggable_app'
    target_project_path = input("Enter path to the target project: ")
    settings_file_path = find_settings_file(target_project_path)

    print(f"Modifying {settings_file_path}")
    
    # Check if the settings file exists
    if settings_file_path:
        modify_settings_file(app_name, settings_file_path)
        print(f"Successfully modified {settings_file_path}")
    else:
        print("Settings file not found in the target project directory.")

if __name__ == "__main__":
    install()
