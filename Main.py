from PIL import Image
from ANSI import ansiArt
from ASCII import asciiArt
from ASCIIrefactor import ascii_refactor


def main(image, new_width, typeOperation):
    img = Image.open(image)

    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)

    img = img.resize((new_width, new_height))
    pixels = img.convert('L').getdata()

    chars = [" ", ".", "'", ",", ";", ":", "c",
             "l", "o", "d", "x", "k", "O", "0",
             "K", "X", "N", "W", "M"]
    char_img = [chars[pixel // 14] for pixel in pixels]
    char_img = ''.join(char_img)

    if typeOperation == 1:
        ascii_image = asciiArt(img, char_img)
        print(ascii_image)
    elif typeOperation == 2:
        ansi_image = ansiArt(img, char_img)
        print(ansi_image)
    elif typeOperation == 3:
        asciiArt(img, char_img)
        ascii_refactor()
    else:
        print("Несуществующий тип")
