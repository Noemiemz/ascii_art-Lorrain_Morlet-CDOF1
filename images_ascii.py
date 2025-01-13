import cv2
import numpy as np

image_path = 'images/monalisa.jpg'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

intensity_matrix = np.array(gray_image)

densities = " ░▒▓█"

intensity_matrix = intensity_matrix / (intensity_matrix.max() / (len(densities) -1))
intensity_matrix = intensity_matrix.astype(int)



with open('images/monalisa.txt', 'w', encoding='utf-8') as f:
    for row in intensity_matrix:
        for intensity in row:
            print(densities[intensity], end='')
            f.write(densities[intensity])
        f.write('\n')
        print()

