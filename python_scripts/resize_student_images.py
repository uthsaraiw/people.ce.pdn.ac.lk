# Resize all student images to make their size smaller
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image  # pip install pillow

def run():
    imagesPath = "../images/students"
    directory_list = os.listdir(imagesPath)

    for eachFolder in directory_list:
        if "." in eachFolder:
            continue  # skip if not folder
        for eachImage in os.listdir(imagesPath+f"/{eachFolder}"):
            try:
                imagePath = imagesPath+f"/{eachFolder}/{eachImage}"
                image = Image.open(imagePath)
                width, height = image.size
                size = os.path.getsize(imagePath)/1024
                if size > 25 or (height > 300 and width > 300):
                    print(f"{imagePath}, width = {width:5}, height = {height:5}, size = {size:4.4}kb")
                    horizontalPadding = (width-300)/2
                    verticalPadding = (height-300)/2

                    # im1 = im.crop((left, top, right, bottom))
                    new_image = image.crop((horizontalPadding, verticalPadding, horizontalPadding+300, verticalPadding+300))

                    new_image.save(imagePath)
            except:
                print(f"Failed to resize image {imagePath}")


if __name__ == "__main__":
    run()
