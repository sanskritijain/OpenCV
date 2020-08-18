import cv2 
from matplotlib import pyplot as plt
 
img = cv2.imread("dog.jpg")
cv2.imshow('Dog image', img) 

gray = cv2.imread('dog.jpg' , cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray dog' ,gray)
