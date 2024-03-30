
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from draw_landmarks_on_image import draw_landmarks_on_image

model_path = 'D:/IA_MOUSE/hand_landmarker.task'
base_options = python.BaseOptions(model_asset_path = model_path)

options = vision.HandLandmarkerOptions(base_options = base_options,
                                       num_hands = 2)

detector = vision.HandLandmarker.create_from_options(options)

img = mp.Image.create_from_file('images/img4.png')

detection_result = detector.detect(img)

annotated_image = draw_landmarks_on_image(img.numpy_view(), detection_result)
cv2.imshow('test', cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
