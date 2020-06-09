import numpy as np
import cv2
import sys


def getImage(img):
    image = img[0]
    image = cv2.imread(image)
    h, w, channel = image.shape
    print(image.shape)
    newImage = np.zeros((h, w, channel), dtype = 'uint8')
    cv2.imshow('in', image)
    for i in range(h):
        for j in range(w):
            for c in range(channel):
                if c == 0:
                    if image[i][j][c] >= 150:
                        newImage[i][j][c] = 32
                    else:
                        newImage[i][j][c] = 255
                if c == 1:
                    if image[i][j][c] >= 150:
                        newImage[i][j][c] = 31
                    else:
                        newImage[i][j][c] = 255
                if c == 2:
                    if image[i][j][c] >= 150:
                        newImage[i][j][c] = 31
                    else:
                        newImage[i][j][c] = 255
    return newImage

if __name__ == "__main__":
    print(sys.argv[1:][0])
    img1 = getImage(sys.argv[1:])
    cv2.imshow('result',img1)
    cv2.waitKey(0)
    postf = sys.argv[1:][0] + 'modified.png'
    cv2.imwrite(postf, img1)


