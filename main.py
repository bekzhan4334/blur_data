import cv2
import pytesseract

# path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# location of the image
img = cv2.imread('images\exmple.png')
# converting to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# config for better quality of detecting
config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(img, config=config)

for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        if el[11]=='ANDREI':
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            # Grab ROI with Numpy slicing and blur

            ROI = img[y:y + h, x:x + w]
            blur = cv2.GaussianBlur(ROI, (23, 23), 0)
            img[y:y + h, x:x + w] = blur
    except IndexError:
        print('No data in the image')
# Insert ROI back into image

# show photo
cv2.imshow('Result',img)
cv2.waitKey(0)