import os
import shutil

def list_files_in_current_directory(directoryPath):
    # List off files from that directory
    files = [f for f in os.listdir(directoryPath) if os.path.isfile(os.path.join(directoryPath, f))]
    
    return files

def cut_extension(filesWithExtension):
    filesWOExtension = []

    for file in filesWithExtension:
        filesWOExtension.append(file.split(".")[0])

    return filesWOExtension

def add_extension(filesWOExtension, extension):
    filesWithExtension = []

    for file in filesWOExtension:
        filesWithExtension.append(file + extension)

    return filesWithExtension

def create_folder(folder_path):
    # Check if the folder already exists
    if not os.path.exists(folder_path):
        # If not, create the folder
        os.makedirs(folder_path)
        print(f"\nFolder '{folder_path}' created successfully.\n")
    else:
        print(f"\nFolder '{folder_path}' already exists.\n")

def move_files_with_text(src_folder, dest_folder, uselessFiles):
    for file in uselessFiles:
        # Construct the full path of the source file
        src_file = os.path.join(src_folder, file)
        # Construct the full path of the destination file
        dest_file = os.path.join(dest_folder, file)
        # Move the file to the destination folder
        try:
            shutil.move(src_file, dest_file)
            print(f"Moved {file} to {dest_folder}")
        except FileNotFoundError:
            print(f"File {file} not found.")
        except PermissionError:
            print(f"Permission denied to move file {file}.")

if __name__ == "__main__":
    # Get the directory where the script and the JPGs are located
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    cr3Path = os.path.join(scriptPath, "cr3")
    trashPath = os.path.join(scriptPath, "0trash")

    jpgFiles = cut_extension(list_files_in_current_directory(scriptPath))
    cr3Files = cut_extension(list_files_in_current_directory(cr3Path))

    print("\nJPG files:")
    for file in jpgFiles:
        print(file)

    print("\nCR3 files:")
    for file in cr3Files:
        print(file)

    print("\nFiles what are going to be moved and later deleted:")
    uselessFiles = set(cr3Files) - set(jpgFiles)
    for file in uselessFiles:
        print(file)

    uselessFiles = add_extension(uselessFiles, ".cr3")
    print("\nSame files with extension:")
    for file in uselessFiles:
        print(file)

    trash = create_folder(trashPath)

    move_files_with_text(cr3Path, trashPath, uselessFiles)

input("\nApasă Enter pentru a închide programul...")
