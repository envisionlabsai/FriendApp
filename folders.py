import os

# Define the base directory where you want to create the structure
base_dir = r"C:\Users\theri\OneDrive\Desktop\FriendApp"

# Define the folder structure you want to create
folders = [
    "app",
    "app/static",
    "app/templates",
    "app/routes",
    "app/models",
    "app/forms",
]

# Create the folders
for folder in folders:
    path = os.path.join(base_dir, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")

# Optionally, create the necessary files
files = {
    "app/__init__.py": "",
    "app/routes.py": "",
    "app/models.py": "",
    "app/forms.py": "",
}

for file, content in files.items():
    path = os.path.join(base_dir, file)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")
