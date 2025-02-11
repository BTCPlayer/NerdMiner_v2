#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from PIL import Image
import sys
import os

def convert_to_16bit_rgb(r, g, b):
    r = (r >> 3) & 0x1F
    g = (g >> 2) & 0x3F
    b = (b >> 3) & 0x1F
    return (r << 11) | (g << 5) | b

def image_to_header(image_file, output_file):
    image = Image.open(image_file)
    image = image.convert('RGB')
    width, height = image.size
    pixels = np.array(image)

    header_content = f"// Generated from {os.path.basename(image_file)}\n"
    header_content += f"const uint16_t {os.path.splitext(os.path.basename(image_file))[0]}Width = {width};\n"
    header_content += f"const uint16_t {os.path.splitext(os.path.basename(image_file))[0]}Height = {height};\n"
    header_content += f"const unsigned short {os.path.splitext(os.path.basename(image_file))[0]}Screen[{width * height}] PROGMEM = {{\n"

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            rgb_16bit = convert_to_16bit_rgb(r, g, b)
            header_content += f"0x{rgb_16bit:04X}, "
        header_content += "\n"

    header_content += "};\n"

    with open(output_file, 'w') as file:
        file.write(header_content)

    print(f"Header file saved as {output_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python image_to_header.py <input_image_file> <output_header_file>")
        sys.exit(1)

    input_image_file = sys.argv[1]
    output_header_file = sys.argv[2]

    image_to_header(input_image_file, output_header_file)

if __name__ == "__main__":
    main()