import cv2

cap=cv2.VideoCapture('joker.mp4')

while cap.isOpened():
    #capture frame by frame
    ret,frame=cap.read()
    #set the frame color to backgrond gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('video',gray)
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
#release the frame
cap.release()
cv2.destroyAllWindows()
