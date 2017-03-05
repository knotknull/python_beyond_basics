#!/usr/bin/python3.5
import math


def mandel(real, imag):
    """ COmpute a point in the Mandelbrot set.

    The logarithm of number of iterations needed to
    determine whether a complex point is in the Mandelbrot set.

    Args:
        real: The real coordinate
        imag: The imaginary coordinate
    Returns:
        An integer in the range 1 - 255.
    """

    x = 0
    y = 0
    for i in range(1, 257):
        if x * x + y * y > 4.0:
            break
        xt = real + x * x - y * y
        y = imag + 2.0 * x * y
        x = xt
    # print( x={}, y={}, xt={}, math.log(i)*256={}, math.log(256) = {}".format(
    # x, y, xt, math.log(i) * 256, math.log(256)))
    # print(" return int(math.log(i) * 256 / math.log(256)) - 1  = ",
    # int(math.log(i) * 256 / math.log(256)) - 1)
    return int(math.log(i) * 256 / math.log(256)) - 1


def mandelbro(size_x, size_y):
    """Make a Mandelbrot set image.

    Args:
        size_x: Image width
        size_y: Image height

    Returns:
        A list of lists of integers in the range of 0 - 255.
    """
    # NOTE: Ooooh Look!!! A nested list compression to return a list of lists
    #
    return[[mandel((3.5 * x / size_x) - 2.5,
                   (2.0 * y / size_y) - 1.0)
            for x in range(size_x)]     # inner list increasing x (width)
           for y in range(size_y)]      # outer list increasing y (height)
