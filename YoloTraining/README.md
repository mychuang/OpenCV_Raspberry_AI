# Yolo trainning mask png
Refer: https://weirenxue.github.io/2021/06/10/YOLOv4_On_Face_Mask_Detection/
## Data set
- The data set were download https://www.kaggle.com/datasets/andrewmvd/face-mask-detection?resource=download

- Set classId=0 is with_mask; classId=1 is without_mask; classId=2 is mask_weared_incorrect

- The Yolo label txt was translated from VOC, the formate was shown below: <br>
```
classId xCenter yCenter bndBoxW bndBoxH
```
- Check the translating code: voc2txt.py

- check the spiltDataset.py, which can spilt to Trainning & Validation data set

## Build Darknet in Windows10 & windows11
Refer: https://github.com/AlexeyAB/darknet#requirements-for-windows-linux-and-macos

- clone (上面的網址) Github source code
- download OpenCV c++版本 (https://sourceforge.net/projects/opencvlibrary/)
- 將下載好的 opencv 搬到 C槽，所以應該在c槽能看到 C:/opencv/build
- 新增系統環境變量:OpenCV_DIR = C:/opencv/build (不會可以跳過)
- 用VS2019打開 darknet/build/darknet/darknet_no_gpu.sln (因為我沒有GPU，有GPU可以選darknet.sln)
- In VS2019 Configuration 改成Release x64
- In VS2019 修改專案屬性(右邊欄，右鍵點選專案darknet_no_gpu)
- In VS2019 property, select Linker/General/Additional Library Directories, 修改OpenCV路徑
- In VS2019 property, select C/C++/General/Additional Include Directories, 修改OpenCV路徑
- 按確定，一樣右鍵專案選Build，應該就成功，成功可在darknet/build/darknet/x64 找到exe檔

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