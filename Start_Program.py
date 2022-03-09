import argparse
import Main


def start():
    q = "Программа для создания ASCII/ANSI art"
    parser = argparse.ArgumentParser(description=q)
    parser.add_argument('--image', '-i', type=str,
                        required=True, help='Image')
    parser.add_argument('--width', '-w', default=250, type=int,
                        required=False, help='Width Image')
    parser.add_argument('--type', '-t', default=1, type=int,
                        required=False, help='Type final Image')
    arguments = parser.parse_args()
    Main.main(arguments.image, arguments.width, arguments.type)


if __name__ == "__main__":
    start()
