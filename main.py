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
        x,y,w,h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img,(x,y), (w+x,h+y),(0,0,255),1)
    except IndexError:
        print('Операция была пропущена')
# show photo
cv2.imshow('Result',img)
cv2.waitKey(0)