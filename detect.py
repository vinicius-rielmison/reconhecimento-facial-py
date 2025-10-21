import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascede = cv2.CascadeClassifier('haarcascade_eye.xml') 

cap = cv2.VideoCapture(0)



while True:
    ret , video = cap.read()


    video = cv2.flip(video,1)

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces :
        cv2.rectangle(video,(x,y) , (x+w,y+h), (255,0,0),2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = video[y:y+h , x:x+w]

        print(int(x+w/2),int(y+h/2))

        eyes = eye_cascede.detectMultiScale(roi_gray)



        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)



    cv2.imshow('Reconhecimento Facial', video )

    Key = cv2.waitKey(1) & 0xFF

    if Key == 27 :
        break


cap.release()
cv2.destroyAllWindows()    
