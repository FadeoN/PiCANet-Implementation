import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from fnmatch import fnmatch

root_dir = "D:\\Git\\SAKE - ORIGINAL\\SAKE\\dataset\\TUBerlin\\images"
save_dir = "D:\\Git\\SAKE - ORIGINAL\\SAKE\\dataset\\TUBerlin\\masks"


pattern1 = "*.jpg"
pattern2 = "*.JPEG"

img_paths = []
for path, subdirs, files in os.walk(root_dir):

    for name in files:
        if fnmatch(name, pattern1) or fnmatch(name, pattern2):
            img_path = os.path.join(path, name)
            
            img = cv2.imread(img_path, 0)

            img = np.where(img > 5 , 255., 0)

            save_path = os.path.join(save_dir, *img_path.split("\\")[-3:-1])

            os.makedirs(save_path, exist_ok=True)

            save_path = os.path.join(save_path, img_path.split("\\")[-1])
            cv2.imwrite(save_path, img)

    
    print("Done")



# for path in img_paths:
#     cur_path = os.path.join(initial_path, path)
#     print(cur_path)
#     img = cv2.imread(cur_path, 0)

#     img = np.where(img > 5 , 255., 0)
#     cv2.imwrite("D:/masks/"+path,img)

# print(img[0][:10])
# print("boo")
# print(img.shape)

# plt.imshow(img, cmap="gray")
# plt.show()


# plt.imshow(img, cmap="gray")
# plt.show()


# kernel = np.ones((5,5),np.uint8)
# img = cv2.erode(img,kernel,iterations = 1)

# plt.imshow(img, cmap="gray")
# plt.show()

# img2 = cv2.dilate(img,kernel,iterations = 5)

# img2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=5)
# # img2 = np.where(img2 > 50, 255., 0.)

# # img2 = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernel, iterations=5)
# img2 = cv2.dilate(img2,kernel,iterations = 5)

# print((img - img2).sum())

# print(img2.shape)
# print(img2[0][:10]) 
# plt.imshow(img2, cmap="gray")
# plt.show()
