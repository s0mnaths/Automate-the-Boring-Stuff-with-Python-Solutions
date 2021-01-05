import os
from PIL import Image,ImageDraw,ImageFont

file=open('guests.txt')
NamesList=file.readlines()

for Name in NamesList:
    card = Image.new('RGBA', (360, 288), (41, 45, 65))
    flower = Image.open('flower.png').convert('RGBA')
    flower=flower.resize((360,288))
    card.paste(flower, (0, 0), flower)

    drawObj = ImageDraw.Draw(card)
    fontFolder = 'usr/share/fonts/TTF'
    fontBlue = ImageFont.truetype(os.path.join(fontFolder,'DejaVuSerif.ttf'), 30)
    drawObj.text((123, 83), Name, fill='blue', font=fontBlue)
    fontGreen = ImageFont.truetype(os.path.join(fontFolder,'DejaVuSerif.ttf'), 30)
    drawObj.text((120, 80), Name, fill=(174, 232, 197), font=fontGreen)
    drawObj.rectangle((5, 5, 355, 283), outline='grey')

    card.save('{}-invite.png'.format(Name))