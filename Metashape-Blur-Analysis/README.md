# Metashape Blur Analysis

- Python script to leverage the Image Quality tool found within Agisoft Metashape developed primarily for photogrammetry workflow
- Blurry images affect photogrammetry negatively, it is better to remove them from the input
- A symbolic link is created for each image with the 'Image/Quality' value as calculated by Metashape in the filename
- This can be used to sort and discard low quality images

## Running
- Install Agisoft Metashape in the default location so that the metashape.exe executable is located in C:\Program Files\Agisoft\Metashape Pro
- Place the .py and .bat file into the directory with the images to be analysed and execute the .bat file
- Elevated privileges (UAC) are required by Windows to create symlinks