from PIL import Image, ImageDraw, ImageFont
import textwrap


class TitlePic:

    def __init__(self, text,date,author):
        self.title = text
        self.date = date
        self.author = author

    def makePic(self):
        offset = 0
        fontsize = 1
        font = ImageFont.truetype("Helvetica.ttf", fontsize)

        img = Image.new('RGB', (1920, 1080), color=(0, 0, 0))

        d = ImageDraw.Draw(img)

        font = ImageFont.truetype("Helvetica.ttf", 75)
        d.text((200, 100), '/u/' + self.author + ":", fill=(255, 255, 255), font=font)

        while(font.getsize(self.title)[0]*font.getsize(self.title)[1]<1920*1080/2):
            fontsize +=1
            font = ImageFont.truetype("Helvetica.ttf", fontsize)

        fontsize -=10
        font = ImageFont.truetype("Helvetica.ttf", fontsize)

        sizeadd = 0
        x=0
        for c in self.title:
            x+=1
            sizeadd += font.getsize(c)[0]
            if(sizeadd>=1920):
                break
        x-=5
        for line in textwrap.wrap(self.title, x):
            d.text((20,200+offset),line,font=font)
            offset+=font.getsize(self.title)[1]

        img.save(self.date + '/' + 'titlepic' + '.png')