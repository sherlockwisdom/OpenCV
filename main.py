#!/bin/python


import cv2 as opencv

# image = 3D array
image = opencv.imread("wrench.jpg")

opencv.imshow("wrench", image)
opencv.waitKey()

B, G, R = opencv.split( image )
opencv.imshow("Red", R)
opencv.waitKey()
opencv.imshow("Green", G)
opencv.waitKey()
opencv.imshow("Blue", B)
opencv.waitKey()

# Blue has been advanced
merged = opencv.merge([B + 100, G, R])
opencv.imshow("Merged image", merged)
opencv.waitKey()

# Image is greyscale
gray_image = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
opencv.imshow("gs_wrench", gray_image)
opencv.waitKey()


print("BGR value:", B, G, R)
print(f"Color image: {image.shape} -> 3 == channel(RGB)")
print(f"Grayscale image: {gray_image.shape}")

GS_val = gray_image[0, 0]
print("GS_val:", GS_val)

hsv_gray_image = opencv.cvtColor(image, opencv.COLOR_BGR2HSV)
print("HSV_val:", hsv_gray_image.shape)
opencv.imshow("gs_wrench", hsv_gray_image)
opencv.waitKey()
opencv.imshow("gs_wrench", hsv_gray_image[:, :, 0])
opencv.waitKey()
opencv.imshow("gs_wrench", hsv_gray_image[:, :, 1])
opencv.waitKey()
opencv.imshow("gs_wrench", hsv_gray_image[:, :, 2])


opencv.waitKey()
