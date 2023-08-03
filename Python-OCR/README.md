# Python OCR

Recreating OCR tool originally written in Matlab in Python to gain experience in Python. The tool was originally written to assist with data analysis for a Flinders University lab (PHYS2712 (Thermodynamics and Energy Systems) 2020). The lab required the students to boil water in a Marcet Boiler and monitor the pressure and temperature and establish a relationship between them. The sensors displayed their readings on a readout but no logging option was available. A phone camera was setup to record the readouts.

In order to convert the video frame image data to a log of readings over time a Matlab OCR utility was written to process each frame and produce text conversion. The Matlab code looped through a directory of edited images and performed OCR using provided areas of interest (AOIs) and a list of expected characters. `ocr(I, roi, 'TextLayout','Word', 'CharacterSet','0123456789')` This utility was built to perform on a specific input and some post OCR data sanitisation was performed. A text progress percentage was output to the command window and updated for each new image, as there were over 50,000 images and some indication of progress was essential.

## Pseudo code
```python
areas_of_interest = [[], [], [], [], []]

CONFIDENCE_THRESHOLD = 0.7
character_set = ['TextLayout','Word', 'CharacterSet','0123456789']
input_folder = r"C:\User\user\Desktop\images"
output_path = r"C:\User\user\Desktop\images_ocr.csv"
images = find_files(input_folder, [".jpg",".jpeg"])

output = []
for image in images:
    I = open(image, 'a+')
    for i, aoi in enumerate(areas_of_interest):
        ocr_text, confidence  = ocr(I, area_of_interest, character_set)
        if confidence > CONFIDENCE_THRESHOLD:
            output[i].append(ocr_text)
    I.close()

header = [[], [], [], [], []]
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(output)
```