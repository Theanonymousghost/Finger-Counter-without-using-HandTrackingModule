import cv2
import numpy as np

def count_fingers(contour):
    hull = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull)

    count = 0
    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, _ = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            # Use cosine rule to find the angle between all points
            a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))

            # Ignore angles > 90 degrees and highlight the rest with dots
            if angle <= np.pi / 2:
                count += 1

    return count

def hand_and_finger_counter(video_path=0):
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading the frame. ")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Use adaptive thresholding
        _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # Find contours
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours based on area
        valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

        # Draw contours on the original frame
        cv2.drawContours(frame, valid_contours, -1, (0, 255, 0), 2)

        # Count fingers for each valid contour
        finger_counts = [count_fingers(cnt) for cnt in valid_contours]

        # Display the frame with finger count
        for i, count in enumerate(finger_counts):
            cv2.putText(frame, f"Fingers: {count}", (10, 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand and Finger Counter", frame)

        # Break the loop if a key is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

hand_and_finger_counter()
