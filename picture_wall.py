# 生成照片墙
import PIL.Image as Image
import os
import math
class My_pho_wall:
    def __init__(self, path, key):
        self.path = path
        self.key_word = key
        self.width = 0
        self.height = 0


    # 设置单个照片的大小
    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)


    # 获取照片
    def get_pic(self):
        pic_list = os.listdir(self.path)
        pic_list.sort()
        pic_num = len(pic_list)
        pic_row_num = int(math.sqrt(pic_num))
        if pic_num%pic_row_num == 0:
            pic_col_num = pic_num // pic_row_num
        else:
            pic_col_num = pic_num // pic_row_num + 1

        print('I got %d pictures and %d pictures in one row, %d pictures in one column.'%(pic_num, pic_row_num, pic_col_num))
        return pic_list, pic_row_num, pic_col_num


    def compose_pic(self):
        pic_list, pic_row_num, pic_col_num = self.get_pic()
        # 新建一块画布，图片见间隔为 10
        canvas = Image.new('RGB', (self.width*pic_row_num+10*(pic_row_num-1), self.height*pic_col_num+10*(pic_col_num-1)))
        x = 0
        y = 0
        for i in pic_list:
            try:
                path_i = self.path + '\\' + i
                img = Image.open(path_i)  # 打开图片
            except IOError:
                print("Error: 没有找到文件或读取文件失败", i)
            else:
                img = img.resize((self.width, self.height), Image.ANTIALIAS)  # 缩小图片
                canvas.paste(img, (x*(self.width+10), y*(self.height+10)))  # 拼接图片
                x += 1
            if x == pic_row_num:
                x = 0
                y += 1
        # 保存图片
        os.getcwd()
        canvas.save(self.key_word + ".jpg")

if __name__ == "__main__":
    path = r"C:\Users\Dell\Pictures\my_pig"
    key = "My Pig"

    my_pho_wall = My_pho_wall(path, key)
    my_pho_wall.size = 256, 325
    my_pho_wall.compose_pic()