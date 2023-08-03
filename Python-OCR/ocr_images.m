clear;
%set Region Of Interest boxes [x, y, x size, y size] starting with pixel 1,1 in top left
box_regions(1,:) = [1 19 124 42];
box_regions(2,:) = [1 104 124 42];
box_regions(3,:) = [1 181 124 42];
box_regions(4,:) = [1 259 124 42];
box_regions(5,:) = [1 344 124 42];
box_regions(6,:) = [1 424 124 42];
box_regions(7,:) = [1 508 124 42];
box_regions(8,:) = [1 603 124 42];

recognition_threshold = 0;

myDir = uigetdir; %gets directory
myFiles = dir(fullfile(myDir,'*.jpg')); %gets all jpg files in struct

output = NaN(length(myFiles),8); %prealloc array for ocr output

prog = 0;
fprintf(1,'Progress: %3d%%\n',prog);

for i = 1:length(myFiles) %each image within folder
    prog = (100*(i/length(myFiles)));
	fprintf(1,'\b\b\b\b%3.0f%%',prog); % Deleting 4 characters (The three digits and the % symbol)
    baseFileName = myFiles(i).name;
    fullFileName = fullfile(myDir, baseFileName);
    I = imread(fullFileName);

    for j = 1:8 %ocr each box
        roi = box_regions(j,:);
        ocrResults = ocr(I, roi, 'TextLayout','Word', 'CharacterSet','0123456789');
        if ocrResults.WordConfidences > recognition_threshold
            output(i,j) = str2double(ocrResults.Words(1,1));
        end
%         show confidence levels
%     Iocr = insertObjectAnnotation(I, 'rectangle', ...
%         ocrResults.WordBoundingBoxes, ...
%         ocrResults.WordConfidences);
%     figure; imshow(Iocr);
    end

end

% process data
output(:,1) = output(:,1)/10 + 273; %add decimal back in and convert to K
output(:,2) = output(:,2)/10; %add decmial
output(:,5) = output(:,5)/10 + 273; %add decimal back in and convert to K
output(:,8) = round(10.^(output(:,8)/10^4));

for i = 1:size(output,1)
    output(i,7) = round(10.^7/output(i,7),1);
end

writematrix(output, 'output.xlsx');
