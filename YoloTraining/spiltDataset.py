import os
import numpy as np

currentPath = os.getcwd()
destination = os.path.join(currentPath, r'yolo_data')

files = os.listdir(destination)
pngList = []

for filename in files:
    if os.path.splitext(filename)[1] != '.txt':
        pngList.append(filename)
np.random.shuffle(pngList)

numTrainingData = int(len(pngList) * 0.8)

with open(os.path.join(currentPath, 'train.txt'), 'w', encoding='UTF-8') as outfile:
    for filename in pngList[:numTrainingData]:
        outfile.writelines(os.path.join(destination, filename) + '\n')

with open(os.path.join(currentPath, 'val.txt'), 'w', encoding='UTF-8') as outfile:
    for filename in pngList[numTrainingData:]:
        outfile.writelines(os.path.join(destination, filename) + '\n')