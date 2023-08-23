# Metashape python script to calculate image quality
# Michal Cedrych 2022
# https://agisoft.freshdesk.com/support/solutions/articles/31000133141-how-to-run-the-script-in-headless-mode-from-the-command-line

import os, sys, time
import Metashape # type: ignore
time_start = time.time()

FILE_EXTENSIONS = [".jpg", ".jpeg", ".tif", ".tiff"]
COMPATIBLE_MAJOR_VERSION = ["1.7", "1.8"] # list of compatible versions

def findFiles(directory, file_extension):    # directory: str, file_extension: list
    # function that returns list of files in folder, matching one of type
    files = []
    for f in os.scandir(directory):
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in file_extension:
                files.append(f.path)
    return files

def init():
    root_folder = os.path.dirname(sys.argv[0])
    print(root_folder)
    photos = findFiles(root_folder, FILE_EXTENSIONS)
    if len(photos) == 0:
        print("No images found...exiting")
        sys.exit(0)
    else:
        print(f"Found {len(photos)} images")
    return root_folder, photos

def checkCompatibility():
    # check compatibility between metashape executable and this python script
    found_major_version = ".".join(Metashape.app.version.split('.')[:2])
    if found_major_version not in COMPATIBLE_MAJOR_VERSION:
        raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, COMPATIBLE_MAJOR_VERSION))
    else:
        print(f"Metashape version {Metashape.app.version} is compatible with this script")

def createSymbolicLinks(root_folder, photos, chunk):
    for i in range(len(chunk.cameras)):
        source_file = photos[i]
        file_name, file_extension = os.path.splitext(os.path.basename(source_file))
        image_quality = str(int(round(float(chunk.cameras[i].meta['Image/Quality']), 4)*10000))
        destination_dir = os.path.join(root_folder, "analysed-metashape")
        destination_file = os.path.join(destination_dir, image_quality + "-" + file_name + file_extension)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        if os.path.exists(destination_file):
            os.remove(destination_file)
        os.symlink(source_file, destination_file)
    print("Photo quality less than 7000 is considered blurry")

def timeKeeping():
    time_finish = time.time()
    duration = time_finish - time_start
    print(f"Blur analysis completed in " + "{:.3f}".format(duration) + " sec")

def main():
    root_folder, photos = init()
    checkCompatibility()
    doc = Metashape.Document()
    chunk = doc.addChunk()
    chunk = doc.chunk
    chunk.addPhotos(photos)
    chunk.analyzePhotos()
    createSymbolicLinks(root_folder, photos, chunk)
    timeKeeping()

if __name__ == '__main__':
    main()
