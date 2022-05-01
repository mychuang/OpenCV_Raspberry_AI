# Yolo trainning mask png
Refer: https://weirenxue.github.io/2021/06/10/YOLOv4_On_Face_Mask_Detection/

## Build darknet
refer [BUILD.md](BUILD.md)

## Data set
- The data set were download https://www.kaggle.com/datasets/andrewmvd/face-mask-detection?resource=download

- Set classId=0 is with_mask; classId=1 is without_mask; classId=2 is mask_weared_incorrect

- The Yolo label txt was translated from VOC, the formate was shown below: <br>
```
classId xCenter yCenter bndBoxW bndBoxH
```
- Check the translating code: voc2txt.py

- check the spiltDataset.py, which can spilt to Trainning & Validation data set

## YoloV4 setting
- Check the folder cfg, there two file: mask.data & mask.names
  - mask.data: 記錄類別數量(classes)、train.txt 的位置(train)、val.txt 的位置(valid)、mask.names 檔案位置(names)、weights 輸出的路徑 (backup)
  - mask.names: 記錄各類別名稱，第一行名稱對應到 classId=0，以此類推

- 修改 yolov4-tiny-custom.cfg
  ```
  sed -i '212s/255/24/' /home/user/mask_detection/cfg/yolov4-tiny-obj.cfg
  sed -i '220s/80/3/' /home/user/mask_detection/cfg/yolov4-tiny-obj.cfg
  sed -i '263s/255/24/' /home/user/mask_detection/cfg/yolov4-tiny-obj.cfg
  sed -i '269s/80/3/' /home/user/mask_detection/cfg/yolov4-tiny-obj.cfg
  ```
  - goto darknet\build\darknet\x64下，執行 darknet_no_gpu.exe
  ```
   ./darknet_no_gpu.exe detector calc_anchors  [user folder]/OpenCV-Beginner/YoloTraining/cfg/mask.data -num_of_clusters 6 -width 416 -height 416 -showpau

   # get result: anchors = 9, 16,  17, 29,  27, 45,  41, 69,  71,107, 138,154
  ``` 
  - 修改 yolov4-tiny-custom.cfg 的 錨點
  ```
     sed -i '219s/10,14,  23,27,  37,58,  81,82,  135,169,  344,319/ 9, 16,  17, 29,  27, 45,  41, 69,  71,107, 138,154/'  [user folder]/OpenCV-Beginner/YoloTraining/cfg/yolov4-tiny-custom.cfg
     
     sed -i '268s/10,14,  23,27,  37,58,  81,82,  135,169,  344,319/ 9, 16,  17, 29,  27, 45,  41, 69,  71,107, 138,154/'  [user folder]/OpenCV-Beginner/YoloTraining/cfg/yolov4-tiny-custom.cfg
  ```

  ### Trainning
  ```
  .\darknet_no_gpu.exe detector train [user folder]\OpenCV-Beginner\YoloTraining\cfg\mask.data [user folder]\OpenCV-Beginner\YoloTraining\cfg\yolov4-tiny-custom.cfg [user folder]\OpenCV-Beginner\YoloTraining\cfg\yolov4-tiny.conv.29 -map 0,1
  ```