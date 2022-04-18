"""
refer: https://wiki.loliot.net/docs/lang/python/libraries/yolov4/python-yolov4-about/
tensorflow: 2.8.0
opencv: 4.5.4
"""
import cv2
from yolov4.tf import YOLOv4

yolo = YOLOv4()
yolo.config.parse_names("./YoloV4Dataset/coco.names")
yolo.config.parse_cfg("./YoloV4Dataset/yolov4-tiny.cfg")

yolo.make_model()
yolo.load_weights("./YoloV4Dataset/yolov4-tiny.weights", weights_type="yolo")

yolo.summary(summary_type="yolo")
yolo.summary()

yolo.inference(media_path="./img/2.jpg")
#yolo.inference(yolo.inference(media_path="./img/LumensNewer.mov", is_image=False))
#yolo.inference(
#    "./img/LumensNewer.mov",
#    is_image = False,
#    cv_frame_size=(320, 240)
#)

