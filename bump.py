#!/usr/bin/python3.5

""" A module for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
                Each row must be in iterable series of integers in the
                range of 0-255.
    Raises:
        OSError: if the file couldn't be written.
    """
    # NOTE: pixes will be a list of list of integeters.
    #       outer list is rows, inner list is pixel bytes
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()   # The next 4 bytes hold the filesize as a
        bmp.write(b'\x00\x00\x00\x00')  # 32-bit little-endian int. 0's for now

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next 4 bytes hold int offset
        # to the pixel data. Zero placeholder for now.
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')  # Image hdr size in bytes - 40 bytes
        bmp.write(_int32_to_bytes(width))   # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')          # Number of image panes
        bmp.write(b'\x08\x00')          # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompress
        bmp.write(b'\x00\x00\x00\x00')  # Unused pizels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pizels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            # Each row of a bmp file must be a multiple of four bytes long
            # hence, pad row to a multiple  of four bytes
            padding = b'\x00' * (4 - (len(row) % 4))
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Go back and fill in our placeholders (bookmarks)
        # fill in size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

# NOTE:  bitwise operators ahead !!!


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def dimenstions(filename):
    """Determine the dimensions in pixels of a BMP image.

    Args:
        filename: The filename of a BMP file.

    Returns:
        A tuple containing two integers with the width and height in pixels

    Raises:
        ValueError: If the file was not a BMP file.
        OsError: If there was a problem reading the file.
    """
    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))
        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)
        return(_bytes_to_int32(width_bytes),
               _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    """Convert a bytes object containing 4 bytes into  an integer"""
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)
