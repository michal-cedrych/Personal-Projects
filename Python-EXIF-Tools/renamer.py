import os
import PIL
# from Opts import Opts

# path, opts = Opts()

def find_files(directory, file_extension):    # directory: str, file_extension: list
    # function that returns list of files in folder, matching one of type
    files = []

    for f in os.scandir(directory):
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in file_extension:
                files.append(f.path)
                
# date created YYYY-MM-DD
seperator = "_"
name = "mcedrych"
# image unique id
id = int

def main():
    pass

if __name__ == '__main__':
    main()


'''
get directory from getopt
get "--revert" flag for original filename
make list of files in that directory
if --revert, write file back with original filename
get date, "_mcedrych_" string, unique image id
preserve current filename in xmp data
if file exists, check if end of file name is (n), and if not append (1), otherwise append (n+1)
'''