# IMPORTANDO AS CLASSES DE TAREFA DO GESTURE RECOGNIZER
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# MODELO GESTURRE RECOGNIZER
model_path = 'D:/IA_MOUSE/gesture_recognizer.task'

# ESPECIFICANDO O CAMINHO DO MODELO
base_options = mp.tasks.BaseOptions(model_asset_path = model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# ENTRADA DE IMAGEM
img = mp.Image.create_from_file('images/img1.jpg')                          

gesture_recognition_result = recognizer.recognize(img)

