import cv2

xml_haar_cascade = 'haarcascade_frontalface_default.xml'

#carregando class
classiFace = cv2.CascadeClassifier(xml_haar_cascade)

#carregar camera
capturar = cv2.VideoCapture(0)

#definir tamanho
capturar.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
capturar.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

#vai ficar executando ate apertar Q
while not cv2.waitKey(20) & 0xff ==ord("x"):
    ret, frame_color =capturar.read()
    
    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    
    faces = classiFace.detectMultiScale(gray)

    for x, y, w, h in faces:
        cv2.rectangle(frame_color, (x,y), (x+w,y+h),(0,255,0),2)

    cv2.imshow('colorido', frame_color)
    cv2.imshow('cinzinha', gray)

