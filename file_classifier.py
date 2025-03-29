import os

# Define file categories based on extensions
CATEGORIES = {
    'Documents': ['.docx', '.pdf', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Code Files': ['.py', '.cpp', '.js'],
    'Others': []
}

def classify_file(file_path):
    """Classifies a file based on its extension."""
    _, ext = os.path.splitext(file_path)
    for category, extensions in CATEGORIES.items():
        if ext.lower() in extensions:
            return category
    return 'Others'
