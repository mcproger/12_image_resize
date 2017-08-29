# Image Resizer

Little script that allow change size of images and save it by arguments entered by user. Name of result image will contain information about chanched sizes.

## Example:
```
Original image - original_image.jpg (100x200)
Result image - result_image_200x400
```

# Using

User should enter path to original file and few arguments that contain information about change size:

  (If path for resize image does not exist, it will be save in the same directory, that original image)


  - Scale of result image. If it exists, height and width can't be specified:
  ```
  $ python3 image_resize.py original_image_path.jpg --scale 2 --output resize_image_save_path.jpg
  ```
  
  
  - Height of result image. Result width will be calculated automaticaly:
  ```
  $ python3 image_resize.py original_image_path.jpg --height 200 --output resize_image_save_path.jpg
  ```
  
  
  - Width of result image. Result height will be calculated automaticaly:
  ```
  $ python3 image_resize.py original_image_path.jpg --width 200 --output resize_image_save_path.jpg
  ```
  
  
  - Width and height of result image:
  ```
  $ python3 image_resize.py original_image_path.jpg --width 200 --height --output resize_image_save_path.jpg
  ```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
