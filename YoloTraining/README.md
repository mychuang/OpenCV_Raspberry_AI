# Yolo trainning mask png

## Data set
- The data set were download https://www.kaggle.com/datasets/andrewmvd/face-mask-detection?resource=download

- Set classId=0 is with_mask; classId=1 is without_mask; classId=2 is mask_weared_incorrect

- The Yolo label txt was translated from VOC, the formate was shown below: <br>
```
classId xCenter yCenter bndBoxW bndBoxH
```
- Check the translating code: voc2txt.py

- check the spiltDataset.py, which can spilt to Trainning & Validation data set