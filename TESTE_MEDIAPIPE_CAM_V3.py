import cv2
import mediapipe as mp

# CAPTURA FRAMES EM UM VIDEO
cam = cv2.VideoCapture(0)

# UTILIZANDO AS SOLUÇÕES DE DETECÇÃO DE MÃOS DO MEDIAPIPE
hand = mp.solutions.hands
Hand = hand.Hands(2)

# SOLUÇÃO PARA DESENHA OS PONTOS DETCTADOS
draw = mp.solutions.drawing_utils

vef = True

while vef:

    status, frame = cam.read()
    frame_rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = Hand.process(frame_rbg)
    points = results.multi_hand_landmarks

    # IMPRIMIR E DESENHAR AS COORDENADS DOS PONTOS
    if points:
        for point in points:
            #print(points)
            draw.draw_landmarks(frame, point, hand.HAND_CONNECTIONS)
            
    # CASO A CAPTURA PARE O PRESSINAR 'q' E=FECHA O LACO
    if not status or cv2.waitKey(1) & 0xff == ord('q'):
        vef = False
    
    # MOSTRA A IMAGEM DA WEBCAM
    cv2.imshow("cam", frame)
                                
    
