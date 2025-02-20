import mediapipe as mp
import numpy as np
import cv2
import os
import uuid

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
 while cap.isOpened():
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)
    image.flags.writeable = False;

    results = hands.process(image)
    image.flags.writeable = True

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image = cv2.flip(image, 1)
    print('results')

    if results.multi_hand_landmarks:
       for num , hand in enumerate(results.multi_hand_landmarks):
          mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(121, 22, 76),  thickness=2, circle_radius=4),
          mp_drawing.DrawingSpec(color=(11, 66, 76), thickness=4, circle_radius=4),

          )


    cv2.imwrite(os.path.join('Output1', '().jpg'.format(uuid.uuid1())), image)
    cv2.imshow('Hand Tracked' , image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

