import os
import shutil

folder_path = r"C:\Users\omshivay\Downloads"

categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.json', '.xml'],
    'Others': []
}

def get_category(extension):
    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

moved_files = 0
skipped = 0
errors = 0

# Pehle check karo folder exist karta hai ya nahi
if not os.path.exists(folder_path):
    print(f"Error: Folder nahi mila - {folder_path}")
    exit()

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if not os.path.isfile(file_path):
        skipped += 1
        continue

    _, extension = os.path.splitext(filename)

    if not extension:
        skipped += 1
        continue

    category = get_category(extension)
    category_folder = os.path.join(folder_path, category)

    try:
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination = os.path.join(category_folder, filename)

        # File already exist karti hai destination me?
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            destination = os.path.join(category_folder, f"{base}_duplicate{ext}")
            print(f"Duplicate found, renaming: {filename}")

        shutil.move(file_path, destination)
        print(f"Moved: {filename} → {category}/")
        moved_files += 1

    except PermissionError:
        print(f"Permission Error: {filename} ko move nahi kar saka - file already open hai")
        errors += 1

    except Exception as e:
        print(f"Unexpected Error on {filename}: {e}")
        errors += 1

print("------------------------------")
print(f"Total moved: {moved_files}")
print(f"Skipped: {skipped}")
print(f"Errors: {errors}")
print("Done!")