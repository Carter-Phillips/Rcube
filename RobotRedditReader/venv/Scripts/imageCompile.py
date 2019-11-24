from PIL import Image, ImageDraw, ImageFont
import textwrap

class mainClass:
    def __init__(self, mainCom, author, title, date):

        self.mainCom = mainCom
        self.author = author
        self.title = title
        self.date = date

    def makepic(self):
        offset = 0
        fontsize = 1
        font = ImageFont.truetype("Helvetica.ttf", fontsize)

        img = Image.new('RGB', (1920, 1080), color=(0, 0, 0))

        d = ImageDraw.Draw(img)

        while (font.getsize(self.mainCom)[0] * font.getsize(self.mainCom)[1] < 500000):
            fontsize += 1
            font = ImageFont.truetype("Helvetica.ttf", fontsize)

        fontsize -= 3
        font = ImageFont.truetype("Helvetica.ttf", fontsize)

        sizeadd = 0
        x = 0
        for c in self.mainCom:
            x += 1
            sizeadd += font.getsize(c)[0]
            if (sizeadd >= 1720):
                break

        x -= 5
        offset =0
        for line in textwrap.wrap(self.mainCom, x):
            d.text((200, 390 + offset), line, font=font)
            offset += font.getsize(self.mainCom)[1]

        font = ImageFont.truetype("Helvetica.ttf", 75)
        d.text((200, 280), '/u/' + self.author + ":", fill=(255, 255, 255), font=font)

        img.save(self.date + '/' + self.author + '.png')