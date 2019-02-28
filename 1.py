import os
from shutil import copyfile

image_folder = "C:\\Users\\HP\\Desktop\\Darknet\\darknet\\new_model_data\\annotations"
dest = "C:\\Users\\HP\\Desktop\\Darknet\\darknet\\new_model_data\\ann"

if __name__ == '__main__':
    for n, image_file in enumerate(os.listdir(image_folder)):
        print(image_file.split(".")[0])
        copyfile(image_folder+"\\"+image_file, dest+'\\'+image_file.split(".")[0]+'.txt')
