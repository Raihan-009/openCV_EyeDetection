# openCV_EyeDetection
openCV HaarCascade Classifier Based Project

## Necessarry dependencies
<p> You can simply pip to install necessarry module. </p>

<code>pip install opencv-python</code>

-----------------------------------
Haar Cascade Classifier
-----------------------------------

<p>Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.</p>

You can get necessary haarcascade file here :
- [harcascade_frontalface_default.xml](https://github.com/Raihan-009/openCV_EyeDetection/blob/main/haar_face.xml)
- [harcascade_eye.xml](https://github.com/Raihan-009/openCV_EyeDetection/blob/main/haar_eye.xml)

---------------------------------------------------
Project Eye Detection with Haar Cascade Classifier
---------------------------------------------------

> For Static Eye Detection 

```python
import cv2
import eyeTracker as et

img = cv2.imread("/Users/Shinigami/Desktop/openCV_EyeDetection/demoface.jpeg")

tracker = et.eyeDetection(scaleFactor=2)
_, frame = tracker.findEyes(img)
cv2.imshow("Framing", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

<p align = "center">
    <img src = "https://github.com/Raihan-009/openCV_EyeDetection/blob/main/results/staticEyeDetectionExample.png">
</p>


> For Dynamic or Real Time Eye Detection

```python
import cv2
import eyeTracker as et

cap = cv2.VideoCapture(0)
tracker = et.eyeDetection()

while True:
    ret, frame = cap.read()
    if ret:
        _, img = tracker.findEyes(frame)
        cv2.imshow("Framing", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

