import cv2
import eyeTracker as et

img = cv2.imread("/Users/Shinigami/Desktop/openCV_EyeDetection/demoface.jpeg")

tracker = et.eyeDetection(scaleFactor=2)
_, frame = tracker.findEyes(img)
cv2.imshow("Framing", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()