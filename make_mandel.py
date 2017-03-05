#!/usr/bin/python3.5
from pprint import pprint as pp
import fractl
import bump
# import math

# Use an aspect ration of 7 to 4
# pixels = fractl.mandelbro(448, 256)
pixels = fractl.mandelbro(896, 512)
pp(pixels)

bump.write_grayscale('/tmp/gs_mandel.bmp', pixels)

print("dimension = ", bump.dimenstions('/tmp/gs_mandel.bmp'))
