import cv2 as cv

# CAPTURA FRAMES EM UM VIDEO
cam = cv.VideoCapture(0)

vef = True

while vef:

    status, frame = cam.read()

    # CASO A CAPTURA PARE O PRESSINAR 'q' E=FECHA O LACO
    if not status or cv.waitKey(1) & 0xff == ord('q'):
        vef = False

    # MOSTRA A IMAGEM DA WEBCAM
    cv.imshow("cam", frame)
    
