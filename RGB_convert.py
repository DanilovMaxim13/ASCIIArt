from math import sqrt

colors = {
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

firstCH = {
    " ": 'white',
    ".": 'white',
    "'": 'white',
    ",": 'white',
    ";": 'white',
    ":": 'white',
    "c": 'white',
    "l": 'white',
    "o": 'white',
    "d": 'grey',
    "x": 'grey',
    "k": 'grey',
    "O": 'grey',
    "0": 'grey',
    "K": 'grey',
    "X": 'grey',
    "N": 'grey',
    "W": 'grey',
    "M": 'grey',
}


def rgb(rgbPixel):
    distance = {}
    distance[distanceRGB(rgbPixel, 'red')] = 'red'
    distance[distanceRGB(rgbPixel, 'yellow')] = 'yellow'
    distance[distanceRGB(rgbPixel, 'magenta')] = 'magenta'
    distance[distanceRGB(rgbPixel, 'white')] = 'white'
    distance[distanceRGB(rgbPixel, 'green')] = 'green'
    distance[distanceRGB(rgbPixel, 'blue')] = 'blue'
    distance[distanceRGB(rgbPixel, 'cyan')] = 'cyan'
    distance[distanceRGB(rgbPixel, 'grey')] = 'grey'
    distance[distanceRGB(rgbPixel, 'black')] = 'grey'
    return distance[min(distance)]


def rgbSimvol(ch):
    return firstCH[ch]


def distanceRGB(rgbPixel, color):
    return sqrt((rgbPixel[0] - colors[color][0]) ** 2 +
                (rgbPixel[1] - colors[color][1]) ** 2 +
                (rgbPixel[2] - colors[color][2]) ** 2)
