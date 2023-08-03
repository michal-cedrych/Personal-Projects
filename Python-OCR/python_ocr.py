areas_of_interest = [[], [], [], [], []]

CONFIDENCE_THRESHOLD = 0.7
character_set = ['TextLayout','Word', 'CharacterSet','0123456789']
input_folder = r"C:\User\user\Desktop\images"
output_path = r"C:\User\user\Desktop\ocr.csv"
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
