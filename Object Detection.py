from ultralytics import YOLO
import cv2
model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model(frame)
    cv2.imshow("Yolo Object Detection",results[0].plot())
    if cv2.waitKey(1) &0xFF==32:
        break
cap.release()
cv2.destroyAllWindows()
