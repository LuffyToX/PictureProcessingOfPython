# -*- coding: utf-8 -*-
# 制作像素图像

from PIL import Image, ImageDraw, ImageFont


def character_generator(text):
    """ 生成器 => 循环字符串 text """
    while True:
        for i in range(len(text)):
            yield text[i]


def pixel_pic(img_path, save_path, text, font_path, font_size=10):
    """ 生成像素图像 """
    img_raw = Image.open(img_path)  # 读取图像对象
    img_array = img_raw.load()      # 获取像素矩阵

    img_new = Image.new("RGB", img_raw.size, (0, 0, 0))  # 新建画布
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font_path, font_size)

    # 上述字符串添加相应的颜色，写入新建的画布
    ch_gen = character_generator(text)
    for y in range(0, img_raw.size[1], font_size):
        for x in range(0, img_raw.size[0], font_size):
            draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

    # 保存成品图
    img_new.convert('RGB').save(save_path)


if __name__ == "__main__":
    img_path = "D:\\相册\\蠢宝\\32.jpg"
    save_path = "C:\\Users\\15510\\Desktop\\pig.jpg"
    font_path = "C:\\Windows\\Fonts\\simkai.ttf"
    text = "我爱你呀"

    print("***** Start *****")
    pixel_pic(img_path, save_path, text, font_path)
    print("***** End *****")
