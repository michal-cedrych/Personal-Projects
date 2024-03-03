import os, datetime, shutil

def find_files(path, date): # directory: str, date: datetime date
        # function that returns list of files in folder, with modification date after date
        # subfolders is all subfolders under directory
        subfolders, files = [], []
        for f in os.scandir(path):
            if f.is_dir():
                subfolders.append(f.path)
            if f.is_file():
                mdate = datetime.date.fromtimestamp((os.path.getmtime(f)))
                print(mdate)
                if mdate > date:
                    files.append(f.path)
        for p in list(subfolders):
            sf, f = find_files(p, date) # recurse into subfolders
            subfolders.extend(sf)
            files.extend(f)
        return subfolders, files

def copy_files(files, destination_path):
    for f in files:
        num_files += 1
        shutil.copy2(f, destination_path)

num_files = 0

date = datetime.date.today()
date = datetime.date.fromisoformat("2023-08-27")
# source_path = r"D:\iPhone Image Backup"
# destination_path = r"D:\Photos\iPhone"
source_path = r"D:\Photos\iPhone\test\source"
destination_path = r"D:\Photos\iPhone\test\dest"

def main():
    _, files = find_files(source_path, date)
    print(f"Found {len(files)} files")
    copy_files(files, destination_path)
    print(f"{num_files} files copied")

if __name__ == '__main__':
    main()
