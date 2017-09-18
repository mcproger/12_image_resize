from PIL import Image
import argparse
import os


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='Path to directory with image')
    parser.add_argument('--output', type=str,
                        help='Path for output image')
    parser.add_argument('--scale', type=float,
                        help='Scale for increase or decrease image')
    parser.add_argument('--width', type=float,
                        help='Width for increase or decrease image')
    parser.add_argument('--height', type=float,
                        help='Height for increase or decrease image')
    args = parser.parse_args()
    return args


def get_path_to_result_image(args, resize_width, resize_height):
    if args.output:
        path_to_result_image = args.output
        return path_to_result_image
    filename, extension = os.path.splitext(args.filepath)
    path_to_result_image = '{filename}_{resize_width}x{resize_height}{extension}'.format(
        filename=filename,
        resize_width=resize_width,
        resize_height=resize_height,
        extension=extension
    )
    return path_to_result_image


def get_original_image_info(path_to_original):
    original_image = Image.open(path_to_original)
    original_width, original_height = original_image.size
    return original_image, original_width, original_height


def get_resize_info(args, original_width, original_height, image_proportion):
    if args.scale and not args.width and not args.height:
        resize_width = args.scale * original_width
        resize_height = args.scale * original_height
        return resize_width, resize_height
    elif args.width and not args.scale and not args.height:
        resize_width = args.width
        resize_height = args.width / image_proportion
        return resize_width, resize_height
    elif args.height and not args.scale and not args.width:
        resize_width = args.height * image_proportion
        resize_height = args.height
        return resize_width, resize_height
    elif args.height and args.width and not args.scale:
        return args.height, args.width
    else:
        return None


def get_resize_image(original_image, path_to_result_image, resize_width, resize_height):
    resize_image = original_image.resize(
        (resize_width, resize_height), Image.ANTIALIAS)
    resize_image.save(path_to_result_image)


if __name__ == "__main__":
    args = get_console_arguments()
    original_image, original_width, original_height = get_original_image_info(
        args.filepath)
    image_proportion = original_width / original_height
    resize_width, resize_height = get_resize_info(
        args, original_width,
        original_height,
        image_proportion
    )
    resize_image_proportion = resize_width / resize_height
    if image_proportion != resize_image_proportion:
        print('Resized image proportion does not correspond to original image proportion')
    path_to_result_image = get_path_to_result_image(
        args,
        round(resize_width),
        round(resize_height)
    )
    resize_image = get_resize_image(
        original_image,
        path_to_result_image,
        round(resize_width),
        round(resize_height)
    )
