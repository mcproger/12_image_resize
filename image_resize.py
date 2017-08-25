from PIL import Image
import argparse


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='Path to directory with image')
    parser.add_argument('--output', type=str,
                        help='Path for output image')
    parser.add_argument('--scale', type=int,
                        help='Scale for increase or decrease image')
    parser.add_argument('--width', type=int,
                        help='Width for increase or decrease image')
    parser.add_argument('--height', type=int,
                        help='Height for increase or decrease image')
    args = parser.parse_args()
    return args


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    args = get_argparser()
    print(args.scale, args.width)
	