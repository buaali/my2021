import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
source_root = "./testdata/src"
target_root = "./testdata/tgt"
out_root = "./testdata/out/"
for filename in os.listdir(source_root):
    img = cv2.imread(os.path.join(source_root, filename))
    meta_dis = np.reshape(img, -1)
    print(meta_dis)
    y = np.linalg.norm(meta_dis)
    meta_dis = meta_dis / y
    for i in os.listdir(target_root):
        tgt_img = cv2.imread(os.path.join(target_root, i))
        tgt_y = np.linalg.norm(np.reshape(tgt_img, -1))
        out_img = (meta_dis * tgt_y)
        out_img = np.reshape(out_img, (img.shape[0], -1))
        cv2.imwrite(os.path.join(out_root, filename.split()[-1]+'_'+i), out_img)
