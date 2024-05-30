import cv2
import numpy as np

# Baca gambar
image = cv2.imread('jerukk.jpg')

# Konversi gambar dari BGR ke HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definisikan rentang warna oranye dalam ruang warna HSV
lower_orange = np.array([10, 100, 100])
upper_orange = np.array([25, 255, 255])

# Buat masker untuk warna oranye
mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

# Terapkan masker ke gambar asli
result = cv2.bitwise_and(image, image, mask=mask)

# Tampilkan hasil
cv2.imshow('Original Image', image)
cv2.imshow('Orange Mask', mask)
cv2.imshow('Detected Orange Color', result)

# Tunggu sampai ada tombol ditekan, lalu tutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
