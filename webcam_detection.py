
import cv2
import face_recognition
import numpy as np

def run_webcam_detection():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam started. Press Q to quit.")
    frame_count  = 0
    process_every = 3  # Process every 3rd frame for speed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        display_frame = frame.copy()

        if frame_count % process_every == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            rgb_small   = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            face_locs   = face_recognition.face_locations(rgb_small)

            for (top, right, bottom, left) in face_locs:
                top    *= 2; right *= 2; bottom *= 2; left *= 2
                cv2.rectangle(display_frame, (left, top), (right, bottom), (0, 255, 0), 3)
                cv2.rectangle(display_frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                cv2.putText(display_frame, f"Face Detected",
                            (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 1)

            face_count_text = f"Faces: {len(face_locs)}"
            cv2.putText(display_frame, face_count_text, (10, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0), 2)

        cv2.imshow("Face Detection — Press Q to quit", display_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Webcam closed.")

if __name__ == "__main__":
    run_webcam_detection()
