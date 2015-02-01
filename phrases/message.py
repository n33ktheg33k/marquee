#!/usr/bin/python
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

text = (("UNICORNS ", (255, 215, 0)), ("for ", (255, 255, 255)), ("BuBBles", (191, 62, 255)))

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t

print(all_text)
width, ignore = font.getsize(all_text)
print(width)


im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)

x = 0;
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 0), t, c, font=font)
    x = x + font.getsize(t)[0]

#im.save("/home/pi/display16x32/rpi-rgb-led-matrix/test.ppm")
im.save("/home/pi/scrollr/phrases/test.ppm")

os.system("/home/pi/scrollr/phrases/led-matrix 1 test.ppm")
