# -*- coding: utf-8 -*-
"""Group-11_ALA_Project_Image_Manipulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lnToWU7RT5QZqMU8ab5d-SUv2Abjxxfu

##Please add the AU.png file and nature.png file from the drive to the colab files section on the left hand side.
###Made by Group 11
####Paavan Sachde AU2140013
####Utsav Raithatha AU2140019
####Hardagna Mehta AU2140144
####Urmil Jagad AU2140179
####Rahul Patel AU2140205
"""

# Addition of Images

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")
img2 = cv2.imread("/content/nature.png")

arr1 = asarray(img1)
arr2 = asarray(img2)

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

arr = np.zeros((rows,cols,3),dtype = int)

for i in range(rows):
  for j in range(cols):
    for k in range(rgb):
      sum = int(arr1[i][j][2-k]) + int(arr2[i][j][2-k])
      if (sum > 255):
        arr[i][j][k] = 255
      else:
        arr[i][j][k] = sum

arr = arr.astype(np.uint8)

img = im.fromarray(arr)
img.save('addition.png')

print("\nInput 1:\n")
input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nInput 2:\n")
input2 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input2)

print("\nOutput:\n")
output = cv2.imread('addition.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved succesfully as addition.png")

# Subtraction of Images

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")
img2 = cv2.imread("/content/nature.png")

arr1 = asarray(img1)
arr2 = asarray(img2)

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

arr = np.zeros((rows,cols,3),dtype = int)

for i in range(rows):
  for j in range(cols):
    for k in range(rgb):
      diff = int(arr1[i][j][2-k]) - int(arr2[i][j][2-k])
      if (diff < 0):
        arr[i][j][k] = 0
      else:
        arr[i][j][k] = diff

arr = arr.astype(np.uint8)

img = im.fromarray(arr)

img.save('subtraction.png')

print("\nInput 1:\n")
input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nInput 2:\n")
input2 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input2)

print("\nOutput:\n")
output = cv2.imread('subtraction.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved succesfully as subtraction.png")

# Negative Image

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")
arr1 = asarray(img1)

arr = arr1.astype(np.uint16)

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

for i in range(rows):
  for j in range(cols):
    for k in range(rgb):
      diff = 255 - int(arr1[i][j][2-k])
      if (diff < 0):
        arr[i][j][k] = 0
      else:
        arr[i][j][k] = diff

arr = arr.astype(np.uint8)

img = im.fromarray(arr)

img.save('negative.png')

print("\nInput:\n")
input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nOutput:\n")
output = cv2.imread('negative.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved succesfully as negative.png")

# Multiplication of Images

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")
img2 = cv2.imread("/content/nature.png")

arr1 = asarray(img1)
arr2 = asarray(img2)

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

arr = np.zeros((rows,cols,3),dtype = int)

for i in range(rows):
  for j in range(cols):
    for k in range(rgb):
      mul = int(arr1[i][j][2-k])*int(arr2[i][j][2-k])
      arr[i][j][k] = mul/255

arr = arr.astype(np.uint8)

img = im.fromarray(arr)
img.save('multiplication.png')

print("\nInput 1:\n")
input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nInput 2:\n")
input2 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input2)

print("\nOutput:\n")
output = cv2.imread('multiplication.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved succesfully as multiplication.png")

# Mirroring of the image by matrix multiplication

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")

arr1 = asarray(img1)
arr = arr1

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

I = np.zeros((rows,cols,3),dtype = int)

for i in range(rows):
  for j in range(cols):
    if( i + j == rows - 1):
      I[i][j] = 1

arr = arr.astype(np.uint8)
for i in range(rows):
  for j in range(cols):
    c = arr[i][j][0]
    arr[i][j][0] = arr[i][j][2]
    arr[i][j][2] = c

tmp = np.zeros((rows,cols,3),dtype = int)

for i in range(rows):
  for g in range(cols):
    tmp[i][g] = 0
    for j in range(rows):
      tmp[i][g] += arr[i][j]*I[j][g]


tmp = tmp.astype(np.uint8)
img = im.fromarray(tmp)

img.save('Inverse.png')

print("\nInput:\n")
input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nOutput:\n")
output = cv2.imread('Inverse.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved successfully as Inverse.png")

# Channel Splitting of an image into R,G,B

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/nature.png")

arr1 = asarray(img1)
arr = arr1

rows = arr1.shape[0]
cols = arr1.shape[1]
rgb = arr1.shape[2]

for i in range(rows):
  for j in range(cols):
    temp = arr[i][j][0]
    arr[i][j][0] = arr[i][j][2]
    arr[i][j][2] = temp

red = arr.astype(np.uint16)
green = arr.astype(np.uint16)
blue = arr.astype(np.uint16)

for i in range(rows):
  for j in range(cols):
      blue[i][j][0] = 0
      blue[i][j][1] = 0

for i in range(rows):
  for j in range(cols):
      green[i][j][0] = 0
      green[i][j][2] = 0

for i in range(rows):
  for j in range(cols):
      red[i][j][2] = 0
      red[i][j][1] = 0

red = red.astype(np.uint8)
green = green.astype(np.uint8)
blue = blue.astype(np.uint8)

red_channel = im.fromarray(red)
green_channel = im.fromarray(green)
blue_channel = im.fromarray(blue)

red_channel.save('red.png')
green_channel.save('green.png')
blue_channel.save('blue.png')

print("\nInput:\n")
input1 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nRed Channel:\n")
output_red = cv2.imread('red.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output_red)

print("\nGreen Channel:\n")
output_green = cv2.imread('green.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output_green)

print("\nBlue Channel:\n")
output_blue = cv2.imread('blue.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output_blue)

print("\nOutput RGB channels saved succesfully as red.png, green.png, blue.png")

# Transpose of Image

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/Inverse.png")
arr = asarray(img)
rows = arr.shape[0]
cols = arr.shape[1]
rgb = arr.shape[2]

arr = arr.astype(np.uint16)

for i in range(rows):
  j = 0
  #for j in range(cols):
  while (j <= i):
    for k in range(rgb):
      tem = arr[i][j][k]
      arr[i][j][k] = arr[j][i][2-k]
      arr[j][i][2-k] = tem
    j+=1
arr = arr.astype(np.uint8)
img = im.fromarray(arr)
img.save('transpose.png')

print("\nInput:\n")
input1 = cv2.imread('Inverse.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nOutput:\n")
output = cv2.imread('transpose.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved successfully as transpose.png")

# Gray Scale of Image

# using numpy
import numpy as npy

# using matplotlib
import matplotlib.image as img

# using statistics to import mean
# for mean calculation
from statistics import mean

m = img.imread("/content/nature.png")

# determining width and height of original image
w, h = m.shape[:2]

# new Image dimension with 4 attribute in each pixel
newImage = npy.zeros([w, h, 4])
#print( w )
#print( h )

for i in range(w):
  for j in range(h):
	# ratio of RGB will be between 0 and 1
    lst = [float(m[i][j][0]), float(m[i][j][1]), float(m[i][j][2])]
    avg = float(mean(lst))
    newImage[i][j][0] = avg
    newImage[i][j][1] = avg
    newImage[i][j][2] = avg
    newImage[i][j][3] = 1 # alpha value to be 1

# Save image using imsave
img.imsave('grayedImage.png', newImage)

print("\nInput:\n")
input1 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(input1)

print("\nOutput:\n")
output = cv2.imread('grayedImage.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(output)

print("\nOutput image saved successfully as grayedImage.png")

# Convolution of Image using 3*3 kernel

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/AU.png")
arr1 = asarray(img1)


print("What type of image effect do you want to perform?\n")
print("1. Edge Detection")
print("2. Smoothing")
print("3. Motion-blur")
print("4. Raised")
print("5. Sharpening")
print("6. Sharpening 2")
print("7. Box Blur")
print("8. Gaussian Blur")
print("9. Vertical Edge Detection")
print("10. Horizontal Edge Detection")
print("11. Emboss\n")

conv_type = int(input("Enter your input: "))
flag = True

if (conv_type == 1):
  kernel = (1)*np.array([[-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]])

elif (conv_type == 2):
  kernel = (1/10)*np.array([[1, 1, 1],
                           [1, 2, 1],
                           [1, 1, 1]])

elif (conv_type == 3):
  kernel = (1/2)*np.array([[0, 0, 1],
                           [0, 0, 0],
                           [1, 0, 0]])

elif (conv_type == 4):
  kernel = (1)*np.array([[0, 0, -2],
                         [0, 2, 0],
                         [1, 0, 0]])

elif (conv_type == 5):
  kernel = (1)*np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]])

elif (conv_type == 6):
  kernel = (1)*np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])

elif (conv_type == 7):
  kernel = (1/9)*np.array([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]])

elif (conv_type == 8):
  kernel = (1/16)*np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]])

elif (conv_type == 9):
  kernel = (1)*np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])

elif (conv_type == 10):
  kernel = (1)*np.array([[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]])

elif (conv_type == 11):
  kernel = (1/2)*np.array([[-2, -1, 0],
                         [-1, 1, 1],
                         [0, 1, 2]])

else:
  print("\nInput out of range...")
  flag = False

if (flag):
  rows = arr1.shape[0]
  cols = arr1.shape[1]
  rgb = arr1.shape[2]

  arr = arr1.astype(np.uint16)

  for i in range(1,rows-1):
    for j in range(1,cols-1):
      for k in range(rgb):
        sum = 0
        for a in range(i-1,i+2):
          for b in range(j-1, j+2):
            sum = sum + ((arr1[a][b][2-k]) * (kernel[a-(i-1)][b-(j-1)]))
        if (sum < 0):
          arr[i][j][k] = 0
        elif (sum > 255):
          arr[i][j][k] = 255
        else:
          arr[i][j][k] = sum

  arr = arr.astype(np.uint8)
  img = im.fromarray(arr)
  img.save('convolution(3*3).png')

  print("\nInput:\n")
  input1 = cv2.imread('AU.png', cv2.IMREAD_UNCHANGED)
  cv2_imshow(input1)

  print("\nOutput:\n")
  output = cv2.imread('convolution(3*3).png', cv2.IMREAD_UNCHANGED)
  cv2_imshow(output)

  print("\nOutput image saved succesfully as convolution(3*3).png")

# Convolution of Image using 5*5 kernel

import numpy as np
import cv2
from numpy import asarray
from PIL import Image as im
from google.colab.patches import cv2_imshow

img1 = cv2.imread("/content/nature.png")
arr1 = asarray(img1)

print("What type of image effect do you want to perform?\n")
print("1. Gaussian Blur")
print("2. Unsharp Masking")

conv_type = int(input("\nEnter your input: "))
flag = True

if (conv_type == 1):
  kernel = (1/256)*np.array([[1, 4, 6, 4, 1],
                            [4, 16, 24, 16, 4],
                            [6, 24, 36, 24, 6],
                            [4, 16, 24, 16, 4],
                            [1, 4, 6, 4, 1]])

elif (conv_type == 2):
  kernel = (-1/256)*np.array([[1, 4, 6, 4, 1],
                            [4, 16, 24, 16, 4],
                            [6, 24, -476, 24, 6],
                            [4, 16, 24, 16, 4],
                            [1, 4, 6, 4, 1]])

else:
  print("\nInput out of range...")
  flag = False

if (flag):
  rows = arr1.shape[0]
  cols = arr1.shape[1]
  rgb = arr1.shape[2]

  arr = arr1.astype(np.uint16)

  for i in range(2,rows-2):
    for j in range(2,cols-2):
      for k in range(rgb):
        sum = 0
        for a in range(i-2,i+3):
          for b in range(j-2, j+3):
            sum = sum + ((arr1[a][b][2-k]) * (kernel[a-(i-1)][b-(j-1)]))
        if (sum < 0):
          arr[i][j][k] = 0
        elif (sum > 255):
          arr[i][j][k] = 255
        else:
          arr[i][j][k] = sum

  arr = arr.astype(np.uint8)

  img = im.fromarray(arr)
  img.save('convolution(5*5).png')

  print("\nInput:\n")
  input1 = cv2.imread('nature.png', cv2.IMREAD_UNCHANGED)
  cv2_imshow(input1)

  print("\nOutput:\n")
  output = cv2.imread('convolution(5*5).png', cv2.IMREAD_UNCHANGED)
  cv2_imshow(output)

  print("\nOutput image saved succesfully as convolution(5*5).png")