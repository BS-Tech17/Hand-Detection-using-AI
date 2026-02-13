import mediapipe as mp
import cv2
import time
import serial

# ===== CHANGE THIS PORT =====
SERIAL_PORT = "COM3"      # Windows example
# SERIAL_PORT = "/dev/ttyACM0"   # Linux / Raspberry Pi
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

gesture_start = None
UNLOCK_HOLD_TIME = 2
cooldown = False

with mp_hands.Hands(
        min_detection_confidence=0.8,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        detected = False

        if results.multi_hand_landmarks:
            detected = True
            for hand in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand,
                    mp_hands.HAND_CONNECTIONS
                )

        if detected and not cooldown:
            if gesture_start is None:
                gesture_start = time.time()

            if time.time() - gesture_start > UNLOCK_HOLD_TIME:
                print("UNLOCK command sent")
                ser.write(b'UNLOCK\n')
                cooldown = True

        else:
            gesture_start = None

        if not detected:
            cooldown = False

        cv2.imshow("Gesture Unlock", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
ser.close()
cv2.destroyAllWindows()
