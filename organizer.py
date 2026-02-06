import os
import shutil

# Base folder to organize
BASE_FOLDER = "test_files"

# File type categories and extensions
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".js", ".html"],
    "Data": [".csv", ".xlsx"]
}

# Create category folders
for folder in FILE_TYPES.keys():
    os.makedirs(os.path.join(BASE_FOLDER, folder), exist_ok=True)

os.makedirs(os.path.join(BASE_FOLDER, "Others"), exist_ok=True)


# Organize files
for file in os.listdir(BASE_FOLDER):
    file_path = os.path.join(BASE_FOLDER, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(
                    file_path,
                    os.path.join(BASE_FOLDER, folder, file)
                )
                moved = True
                break

        if not moved:
            shutil.move(
                file_path,
                os.path.join(BASE_FOLDER, "Others", file)
            )


print("Files organized successfully")