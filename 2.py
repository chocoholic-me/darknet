import os
path = "C:\\Users\\HP\\Desktop\\Darknet\\darknet\\data\\new_model_data\\images"
path2 = "data/new_model_data/images/"
imgList = os.listdir(path)

txtFile = open("train.txt",'w')

for img in imgList:
    imgPath = path2 + img + '\n'
    txtFile.write(imgPath)