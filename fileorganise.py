import os
import shutil
from datetime import datetime

# Updated mapping of file extensions to their destination folders
folder_mapping = {
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    '.aac': 'Music',
    '.lua': 'Scripts/Lua',
    '.py': 'Scripts/Python',
    '.js': 'Scripts/JavaScript',
    '.css': 'Stylesheets',
    '.html': 'Web',
    '.txt': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.7z': 'Archives',
    '.cpp': 'Source/C++',
    '.h': 'Source/C++',
    '.c': 'Source/C',
    '.java': 'Source/Java',
    '.rb': 'Source/Ruby',
    '.sh': 'Scripts/Shell',
    '.bat': 'Scripts/Batch',
    '.json': 'Data',
    '.xml': 'Data',
    # Add more extensions and destinations as needed
}

def create_backup(files, backup_directory):
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    for filepath in files:
        if os.path.exists(filepath):
            relative_path = os.path.relpath(filepath, start=os.path.dirname(filepath))
            backup_path = os.path.join(backup_directory, relative_path)
            backup_folder = os.path.dirname(backup_path)
            
            if not os.path.exists(backup_folder):
                os.makedirs(backup_folder)
            
            shutil.copy2(filepath, backup_path)
            print(f"Backed up {filepath} to {backup_path}")

def organize_files(directory):
    # Define the backup directory with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_directory = os.path.join(directory, f"backup_{timestamp}")

    files_to_move = []
    
    # Determine which folders are needed and collect files to move
    needed_folders = set()
    for root, dirs, files in os.walk(directory):
        # Skip directories like 'node_modules'
        dirs[:] = [d for d in dirs if d.lower() != 'node_modules']
        
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Get the file extension
            _, ext = os.path.splitext(filename)
            
            # Determine the destination folder
            folder = folder_mapping.get(ext.lower())
            if folder:
                needed_folders.add(folder)
                files_to_move.append(filepath)
    
    # Create backup for files that will be moved
    create_backup(files_to_move, backup_directory)
    
    # Create folders if they are needed
    for folder in needed_folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Move files to their respective folders
    for filepath in files_to_move:
        _, filename = os.path.split(filepath)
        _, ext = os.path.splitext(filename)
        
        # Determine the destination folder
        folder = folder_mapping.get(ext.lower())
        if folder:
            dest_folder = os.path.join(directory, folder)
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    directory = input("Enter the absolute directory path to organize: ").strip()
    organize_files(directory)
