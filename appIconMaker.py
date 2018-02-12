# appIconMaker.py
import cv2
import os

# Create directory and move into it
def mkdir(folder):
  try:
    os.makedirs(folder)
  except OSError:
    pass
  os.chdir(folder)

# image file names
filenames = ["iphone-20@2x.png", "iphone-20@3x.png", "iphone-29@2x.png",
             "iphone-29@3x.png", "iphone-40@2x.png", "iphone-40@3x.png",
             "iphone-60@2x.png", "iphone-60@3x.png", "ipad-20@1x.png",
             "ipad-20@2x.png", "ipad-29@1x.png", "ipad-29@2x.png",
             "ipad-40@1x.png", "ipad-40@2x.png", "ipad-76@1x.png",
             "ipad-76@2x.png", "ipad-83.5@2x.png", "ios-marketing-1024@1x.png"]
# image sizes            
size = [20, 20, 29, 29, 40, 40, 60, 60, 20, 20, 29, 29, 40, 40, 76, 76,83.5,
         1024]

# load image into openCV
img = cv2.imread('Logo.png')

# mkdir and cd into new dir
mkdir("AppIcon.appiconset")

# create new images resized to the above specification
for i in range(0, 18):
    new_img = cv2.resize(img, (size[i], size[i]))
    cv2.imwrite(filenames[i],new_img)
