import os

# Define the folder structure
folders = [
    "assets/images",
    "assets/css",
    "assets/js"
]

files = {
    "index.html": "<!-- Home Page -->",
    "about.html": "<!-- About Me Page -->",
    "projects.html": "<!-- Projects Page -->",
    "skills.html": "<!-- Skills Page -->",
    "blog.html": "<!-- Blog Page -->",
    "contact.html": "<!-- Contact Page -->",
    "assets/css/styles.css": "/* Main Stylesheet */",
    "assets/js/script.js": "// Optional JavaScript file"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("✅ Portfolio structure created successfully!")
