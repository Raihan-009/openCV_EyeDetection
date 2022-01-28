import cv2

class eyeDetection():
    def __init__ (self, scaleFactor=1.1,minNeighbors = 3, flags = 0, minSize = (200,200), maxSize = False):
        self.face_cascade = cv2.CascadeClassifier("/Users/Shinigami/Desktop/openCV_FaceDetection/haar_face.xml")
        self.eye_cascade = cv2.CascadeClassifier("/Users/Shinigami/Desktop/openCV_EyeDetection/haar_eye.xml")
        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize = minSize
        self.maxSize = maxSize

    def findEyes(self,img):
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.faces = self.face_cascade.detectMultiScale(grayImg, self.scaleFactor,self.minNeighbors)
        f_bbox = []
        e_bbox = []
        if (len(self.faces) != 0):
            for x,y,w,h in self.faces:
                f_bbox.append([x,y,w,h])
                #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
                roi_gray = grayImg[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

                self.eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for ex,ey,ew,eh in self.eyes:
                    e_bbox.append([ex,ey,ew,eh])
                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
        return e_bbox, img
def main():
    cap = cv2.VideoCapture(0)
    tracker = eyeDetection()

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

if __name__ == "__main__":
    main()