import cv2
from PIL import Image

img_cat = 'pics/cat.jpeg'
image = cv2.imread(img_cat)

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)

cat = Image.open(img_cat)
glasses = Image.open('pics/glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, w, h) in cat_face:
    #cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h/4 + 5)), glasses)
    cat.save('pics/newCat.png')
    cat_glass = cv2.imread('pics/newCat.png')
    cv2.imshow("Cat", cat_glass)
    cv2.waitKey()