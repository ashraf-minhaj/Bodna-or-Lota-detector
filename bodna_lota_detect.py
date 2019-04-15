"""
"""

import cv2


bodna_lota_classifier = cv2.CascadeClassifier('C:\\Users\\HP\\cv_practice\\bodna_Lota\\bodna_lota_haar_cascade_classifier.xml')
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodnas = bodna_lota_classifier.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in bodnas:
        
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 4)
        
    number = len(bodnas)
    print("Voge noy Tyag ei shukh.\n")
    print(f"{number} Bodna / Lota detected")
    
    cv2.imshow('Bodna / Lota', img)
    if(cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()