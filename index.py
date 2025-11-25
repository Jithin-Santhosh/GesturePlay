import sys
import time

missing = []
try:
    import cv2
except Exception:
    missing.append('opencv-python (cv2)')

try:
    import mediapipe as mp
except Exception:
    missing.append('mediapipe')

try:
    from pynput.keyboard import Controller
except Exception:
    missing.append('pynput')

if missing:
    print('Missing required packages:')
    for m in missing:
        print(f' - {m}')
    print('\nInstall them with:')
    print('    pip install -r requirements.txt')
    sys.exit(1)

keyboard = Controller()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Unable to open camera (VideoCapture returned false).')
    print('If you have multiple cameras, try changing the index in VideoCapture(0).')
    cap.release()
    sys.exit(1)


def press_key(key, duration=0.2):
    # Accept single-character strings; pynput Controller supports them directly.
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)


def main():
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print('Failed to read frame from camera.')
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    # Get coordinates of the index finger tip
                    x = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                    y = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

                    height, width, _ = frame.shape
                    cx, cy = int(x * width), int(y * height)

                    # For simplicity, divide screen into left (A), right (D), up (W), down (S)
                    if cx < width // 3:
                        press_key('a')
                    elif cx > 2 * width // 3:
                        press_key('d')
                    elif cy < height // 3:
                        press_key('w')
                    elif cy > 2 * height // 3:
                        press_key('s')

                    mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Hand Control', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        print('\nInterrupted by user')
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
