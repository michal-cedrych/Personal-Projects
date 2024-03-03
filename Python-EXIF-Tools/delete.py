import os

def find_empty_dirs(path):
    results = []
    for dirpath, dirs, files in os.walk(path):
        if not dirs and not files:
            results.append(dirpath)
    return results

def delete_folders(folders):
    deleted = []
    for folder in folders:
        os.rmdir(folder)
        deleted.append(folder)
    return deleted

path = r"D:\Photos\iPhone\sorting"

def main():
    folders = find_empty_dirs(path)
    if len(list(folders)) != 0:
        print(f"{len(list(folders))} empty folders found, deleting")
        deleted = delete_folders(folders)
        print(f"{len(deleted)} empty folders deleted")
    else:
        print("No empty folders found to delete")

if __name__ == '__main__':
    main()
