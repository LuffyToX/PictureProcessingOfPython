# -*- coding: utf-8 -*-
# 批量修改文件名

import os


def change_filename(file_path):
    print("***** start *****")
    if not os.path.exists(file_path):
        print("目录不存在")
        os.exit(1)
    filenames = os.listdir(file_path)
    i = 0
    for filename in filenames:
        i = i+1
        newname = str(i) + ".jpg"
        print("***** The %dth is ok *****" % i)
        os.rename(file_path + '\\' + filename, file_path + '\\' + newname)


if __name__ == "__main__":
    file_path = "D:\\相册\\蠢宝"
    change_filename(file_path)
