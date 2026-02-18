import cv2
import numpy as np

resim=cv2.imread("mtt.jpg",0)  #imread bir resim okuyacağını belirtir.
cv2.imshow("MTT MTAL",resim) #ilk parametre resmin köşesinde yazacak olan yazı ikincisi imshow komutunun göstereceği resim
cv2.imwrite("yeniresim.png",resim) #üzerinde değişiklik yapılan resmi ayrı olarak kullanmak için

cv2.waitKey(0) #pencere açıldıktan sonra herhangi bir tuşa basılması için bekler
cv2.destroyAllWindows() #opencv ye bağlı tüm pencereleri kapat