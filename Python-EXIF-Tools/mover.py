import os, shutil, datetime

source_path = r"D:\Photos\iPhone\new2"
destination_path =r"D:\Photos\iPhone\sorted"

def main():
    files_moved = 0
    invalid_name = 0
    duplicate = 0
    move_tally = {}
    for dirpath, dirs, filenames in os.walk(source_path):
        if not len(filenames):
            print("No files found")
        else:
            print(f"{len(filenames)} files found")
            print("Moving files...")
        for f in filenames:
            # validate filename has correct format (YYYY-MM-DD)
            try:
                date_str = f[0:10]
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            except:
                invalid_name += 1
                continue # skip to next f in filename if filename doesn't start with correct string
            
            # extract year and month, turn int to 0 padded string
            year = str(date.year).zfill(4)
            month = str(date.month).zfill(2)
            
            # keep track of how many flies are moved into each folder
            tally_folder = year + "\\" + month
            if not move_tally.get(tally_folder): move_tally.update({tally_folder:0}) # create new entry in tally folder if this is a new folder
            
            # construct paths
            original_file_path = os.path.join(dirpath, f)
            new_dirpath = os.path.join(destination_path, year, month)
            new_file_path = os.path.join(new_dirpath, f)
            
            # create new dir if needed
            if not os.path.exists(new_dirpath):
                os.makedirs(new_dirpath)
            
            # move file (rename/replace file path)
            if os.path.exists(new_file_path):
                print(f"{f}: duplicate, skipping")
                duplicate += 1
                continue
            os.replace(original_file_path, new_file_path)
            files_moved +=1
            move_tally[tally_folder] += 1
    
    # print status
    print("\nNumber of files moved into folder:")
    for k, v in move_tally.items():
        print (f"{k} ({v})")
    print()
    if invalid_name: print(f"{invalid_name} files have incorrect name format (should be YYYY-MM-DD)")
    if duplicate: print(f"{duplicate} duplicate files not moved")
    if len(filenames): print(f"{files_moved} / {len(filenames)} files moved")

if __name__ == '__main__':
    main()
