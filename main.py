import cv2
import pytesseract
import re

#patterns
name_pattern = '^[A-Z][-a-zA-Z]+$'
passport_pattern = '^(?!^0+$)[a-zA-Z0-9]{3,20}$'
date_pattern = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9])(?!\d)'

# path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# location of the image
img = cv2.imread('D:\\TG_bots\\data_finder\\images\\example.jpg.jpg')
# converting to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# config for better quality of detecting
config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(img, config=config)
blur_img = img.copy()

for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        if re.match(name_pattern, el[11]) or re.match(passport_pattern, el[11]) or re.match(date_pattern, el[11]):
            #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  => green rectangle
            # Grab ROI with Numpy slicing and blur
            ROI = img[y:y + h, x:x + w]
            blur = cv2.GaussianBlur(ROI, (23, 23), 0)
            blur_img[y:y + h, x:x + w] = blur
    except IndexError:
        print('No data in the image')
# Insert ROI back into image

# show photo
cv2.imshow('Before',img)
cv2.imshow('After',blur_img)
cv2.waitKey(0)