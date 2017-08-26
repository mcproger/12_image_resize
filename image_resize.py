from PIL import Image
import argparse
import os


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='Path to directory with image')
    parser.add_argument('--output', type=str,
                        help='Path for output image')
    parser.add_argument('--scale', type=float,
                        help='Scale for increase or decrease image')
    parser.add_argument('--width', type=int,
                        help='Width for increase or decrease image')
    parser.add_argument('--height', type=int,
                        help='Height for increase or decrease image')
    args = parser.parse_args()
    return args


def get_original_image_info(path_to_original):
    original_image = Image.open(path_to_original)
    original_width, original_height = original_image.size
    return original_image, original_width, original_height


def get_path_to_result_image(args, width, height):
    if args.output:
        path_to_result_image = args.output
        return path_to_result_image
    filename, extension = os.path.splitext(args.filepath)
    path_to_result_image = '{filename}_{width}x{height}{extension}'.format(
        filename=filename,
        width=width,
        height=height,
        extension=extension
    )
    return path_to_result_image


def get_image_resize_area(args, image_proportion, original_width, original_height):
    if args.scale and not args.width and not args.height:
        resize_area = (0, 0, original_width * args.scale,
                       original_height * args.scale)
    elif args.width and not args.height:
        resize_area = (0, 0, args.width, args.width / image_proportion)
    elif args.height and not args.width:
        resize_area = (0, 0, args.height * image_proportion, args.height)
    else:
        resize_area = (0, 0, args.width, args.height)
    return resize_area


def get_resize_image(original_image, path_to_result_image, resize_area):
    resize_image = original_image.crop(resize_area)
    resize_image.save(path_to_result_image)
    return None


if __name__ == '__main__':
    args = get_argparser()
    original_image, original_width, original_height = get_original_image_info(
        args.filepath)
    image_proportion = original_width / original_height
    path_to_result_image = get_path_to_result_image(
        args, original_width, original_height)
    resize_area = get_image_resize_area(
        args, image_proportion, original_width, original_height)
    get_resize_image(original_image, path_to_result_image, resize_area)
