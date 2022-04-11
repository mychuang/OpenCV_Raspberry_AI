import cv2
import numpy as np
from yolov4.tf import YOLOv4

# import Yolo Model
yolo = YOLOv4()
yolo.config.parse_names("./YoloV4Dataset/coco.names")
yolo.config.parse_cfg("./YoloV4Dataset/yolov4-tiny.cfg")

yolo.make_model()
yolo.load_weights("./YoloV4Dataset/yolov4-tiny.weights", weights_type="yolo")

yolo.summary(summary_type="yolo")
yolo.summary()

# rewrite the yolo draw_bboxes function
def draw_bbox(image: np.ndarray, pred_bboxes: np.ndarray):
    frame = np.copy(image)
    height, width, _ = frame.shape
    bboxes = pred_bboxes * np.array([width, height, width, height, 1, 1])

    # only plot person class
    for bbox in bboxes:
        # check id.
        if(bbox[4] == 0.00):
            c_x = int(bbox[0])
            c_y = int(bbox[1])
            half_w = int(bbox[2] / 2)
            half_h = int(bbox[3] / 2)

            # Draw box
            top = c_x - half_w
            if top < 10:
                top = 10
            left = c_y - half_h
            if left < 0:
                left = 0
            bottom = c_x + half_w
            if bottom > height:
                bottom = height
            right = c_y + half_h
            if right > width:
                right = width

            top_left = (top, left)
            bottom_right = (c_x + half_w, c_y + half_h)

            # Draw a bounding box.
            font_size = 0.4
            font_thickness = 2

            cls_id = int(bbox[4])
            prob = bbox[5] #機率
            cv2.rectangle(frame, top_left, bottom_right, (255, 178, 50), 2)

            # Draw text
            bbox_text = "{}: {:.1%}".format("person", prob)
            cv2.putText(
                frame,
                bbox_text,
                (top_left[0], top_left[1] - 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_size,
                (77, 59, 0),
                font_thickness,
                lineType=cv2.LINE_AA,
            )

    return frame

# Open Camera
cap = cv2.VideoCapture(0)

#set video size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 降frame rate 所需的變數
countMax = 20
count = 19

while cap.isOpened():
    try:
        is_success, frame = cap.read()
    except cv2.error:
        continue
    if not is_success:
        break

    # 降 frame Rate
    count = count + 1
    if(count == countMax):
        bboxes = yolo.predict(frame, prob_thresh=0.25)
        count = 0

    image = draw_bbox(frame, bboxes)
    # yolo.draw_bboxes() 可繪製所有類別之物件
    #image = yolo.draw_bboxes(frame, bboxes)

    cv2.imshow("result", image)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()




