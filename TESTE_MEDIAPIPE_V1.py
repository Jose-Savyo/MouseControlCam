# IMPORTANDO AS CLASSES DE TAREFA DO GESTURE RECOGNIZER
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from visualization_utilities import *
from draw_landmarks_on_image import draw_landmarks_on_image

# MODELO GESTURRE RECOGNIZER
model_path = 'D:/IA_MOUSE/gesture_recognizer.task'

# ESPECIFICANDO O CAMINHO DO MODELO
base_options = mp.tasks.BaseOptions(model_asset_path = model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# ENTRADA DE IMAGEM
img = mp.Image.create_from_file('D:/IA_MOUSE/ShootingGameAI-main/images/img1.jpg')

gesture_recognition_result = recognizer.recognize(img)

annotated_image = draw_landmarks_on_image(img.numpy_view(), gesture_recognition_result)
cv2.imshow('test', cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
