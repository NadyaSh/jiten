# -*- coding: utf-8 -*-
import os
from PIL import Image

folder = './1_static/'
width = 10
result = Image.new('RGBA', (160*width, 120*(len(os.listdir(folder))//width+1)))
i = 0
for filename in os.listdir(folder):
  im = Image.open(folder + filename)
  w, h = im.size
  region = im.crop((0, 0, w, h))
  result.paste(region, ((i%width) * 160, (i//width) * 120 ))
  i += 1

result.save('victory1.png', 'PNG')