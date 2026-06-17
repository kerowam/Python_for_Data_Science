from numpy import array
from PIL import Image
from matplotlib import pyplot as plt


def ft_invert(array) -> array:
    '''Inverts the color of the image received.'''
    inverted_image = Image.fromarray(255 - array)
    plt.imshow(inverted_image)
    plt.show()
    return 255 - array


def ft_red(array) -> array:
    '''Converts the image to red channel.'''
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    red_image = Image.fromarray(red)
    plt.imshow(red_image)
    plt.show()
    return red


def ft_green(array) -> array:
    '''Converts the image to green channel.'''
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    green_image = Image.fromarray(green)
    plt.imshow(green_image)
    plt.show()
    return green


def ft_blue(array) -> array:
    '''Converts the image to blue channel.'''
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    blue_image = Image.fromarray(blue)
    plt.imshow(blue_image)
    plt.show()
    return blue


def ft_grey(array) -> array:
    '''Converts the image to grey scale.'''
    gray = array.copy()
    image = Image.fromarray(gray)
    gray_image = image.convert('L')
    gray[:, :, 0] = gray_image
    gray[:, :, 1] = gray_image
    gray[:, :, 2] = gray_image
    plt.imshow(gray_image)
    plt.show()
    return gray
