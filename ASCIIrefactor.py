import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw


def ascii_refactor():
    grayscale = 'L'
    font = PIL.ImageFont.truetype('cour.ttf', size=20)

    with open("ascii_img.txt") as text_file:
        lines = tuple(l.rstrip() for l in text_file.readlines())

    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pointToPixel(font.getsize(test_string)[1])
    max_width = pointToPixel(font.getsize(max_width_line)[0])
    height = max_height * len(lines)
    width = int(round(max_width + 40))
    image = PIL.Image.new(grayscale, (width, height), color=255)
    draw = PIL.ImageDraw.Draw(image)

    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=0, font=font)
        vertical_position += line_spacing

    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    image.save('content.png')


def pointToPixel(size):
    return int(round(size * 96.0 / 72))


if __name__ == "__main__":
    ascii_refactor()
