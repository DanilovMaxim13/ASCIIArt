from termcolor import colored
from RGB_convert import rgb, rgbSimvol


def ansiArt(img, char_img):
    new_pixels = ''
    temp = 0
    for j in range(0, img.size[1]):
        for i in range(0, img.size[0]):
            new_pixels = new_pixels + colored(char_img[temp],
                                              rgbSimvol(char_img[temp]),
                                              "on_" +
                                              rgb(img.getpixel((i, j))),
                                              attrs=['bold'])
            temp = temp + 1

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + img.size[0] * 19]
                   for index in range(0, new_pixels_count, img.size[0] * 19)]
    ascii_image = "\n".join(ascii_image)

    with open("ascii_img.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image
