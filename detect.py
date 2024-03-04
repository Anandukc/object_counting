from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("path to input image")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
line_points = [(455, 336), (678, 331)]

# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi",
                       cv2.VideoWriter_fourcc(*'mp4v'),
                       fps,
                       (1080, 600))  # will be same as image size

# Init Object Counter
counter = object_counter.ObjectCounter()
counter.set_args(view_img=True,
                 reg_pts=line_points,
                 classes_names=model.names,
                 draw_tracks=True,
                 view_in_counts=False,
                 region_thickness=4,
                 count_color=(255,0,0))

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    im0 = cv2.resize(im0, (1080, 600))    # set image size for display
    tracks = model.track(im0, persist=True, show=True, classes=39)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()


    
