def asciiArt(img, char_img):
    new_pixels_count = len(char_img)
    ascii_image = [char_img[index:index + img.size[0]]
                   for index in range(0, new_pixels_count, img.size[0])]
    ascii_image = "\n".join(ascii_image)

    with open("ascii_img.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image
