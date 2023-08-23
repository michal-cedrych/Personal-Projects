import os, datetime

def findFiles(directory, date = None):    # directory: str, file_extension: list
    files = []
    for f in os.scandir(directory, date):
        if f.is_file():
            if f exif modified/created date is date
                files.append(f.path)
    return files

def copyFiles(files, destination_path):~d34d