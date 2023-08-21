import cv2
import numpy as np
y = cv2.imread("C:/Users/Alan/Downloads/d1.jpg")

print (y)

print("- Number of Pixels: " + str(y.size))
print("- Shape/Dimensions: " + str(y.shape))
cv2.imshow('Imagen Original', y)

cv2.waitKey(0)

gray_y = cv2.cvtColor(y, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen Original", y)
cv2.imshow("Imagen en escala de grises", gray_y)

rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 180, .5)
rotatedImage = cv2.warpAffine(y, rotationMatrix, (width, height))
cv2.imshow('Imagen Girada', rotatedImage)
newImg = cv2.resize(y, (0,0), fx=0.75, fy=0.75)
cv2.imshow('Image Cambio de dimensiones', newImg)
cv2.waitKey(0)

newImg = cv2.resize(y, (550, 350))
cv2.imshow('Imagen cambio de dimensiones col', newImg)

contrast_img = cv2.addWeighted(y, 2.5, np.zeros(y.shape, y.dtype), 0, 0)
cv2.imshow('Imagen Original', y)
cv2.imshow('Imagen Contraste', contrast_img)

edge_img = cv2.Canny(y,100,200)
cv2.imshow("Bordes detectados ", edge_img)

blur_image = cv2.GaussianBlur(y, (7,7), 0)
cv2.imshow('Imagen original', y)
cv2.imshow('Imagen Borrosa', blur_image)


cv2.waitKey(0)

#Recortar una imagen
cropped_image = y[310:680, 340:550]
cv2.imshow("Imagen recortada", cropped_image)
cv2.imwrite("C:/Users/Alan/Downloads/d1.jpg", cropped_image)
cv2.waitKey(0)