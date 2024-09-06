import os
import shutil

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

def organize_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The provided path is not a valid directory: {directory}")
        return
    
    # Create folders if they do not exist
    for folder in set(folder_mapping.values()):
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)
        
        # Determine the destination folder
        folder = folder_mapping.get(ext.lower())
        if folder:
            dest_folder = os.path.join(directory, folder)
            
            # Ensure all parent directories exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            # Move the file
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    directory = input("Enter the absolute directory path to organize: ").strip()
    organize_files(directory)
