#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from PIL import Image
import sys
import re

def convert_to_rgb(value):
    r = (value >> 11) & 0x1F
    g = (value >> 5) & 0x3F
    b = value & 0x1F
    # 扩展到8位
    r = (r << 3) | (r >> 2)
    g = (g << 2) | (g >> 4)
    b = (b << 3) | (b >> 2)
    return r, g, b

def parse_header_file(header_file):
    with open(header_file, 'r') as file:
        content = file.read()

    # 提取所有屏幕数据数组
    screens = re.findall(r'const unsigned short (\w+Screen)\[\w+\] PROGMEM =\{(.*?)\};', content, re.DOTALL)
    return screens, content

def extract_dimensions(content, screen_name):
    width_match = re.search(rf'const uint16_t {screen_name[:-6]}Width = (\d+);', content)
    height_match = re.search(rf'const uint16_t {screen_name[:-6]}Height = (\d+);', content)

    if not width_match or not height_match:
        print(f"Could not find dimensions for {screen_name}")
        return None, None

    width = int(width_match.group(1))
    height = int(height_match.group(1))
    return width, height

def main():
    if len(sys.argv) != 2:
        print("Usage: python screen.py <input_header_file>")
        sys.exit(1)

    input_header_file = sys.argv[1]

    try:
        screens, content = parse_header_file(input_header_file)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"Found {len(screens)} screens")

    for screen_name, data in screens:
        print(f"Processing {screen_name}...")

        width, height = extract_dimensions(content, screen_name)
        if width is None or height is None:
            continue

        print(f"Dimensions for {screen_name}: {width}x{height}")

        # 移除注释
        data = re.sub(r'//.*?\n', '', data)
        data = data.replace('\n', '').replace(' ', '').split(',')
        data = [int(x, 16) for x in data if x]

        # 创建空的RGB数组
        rgb_data = np.zeros((height, width, 3), dtype=np.uint8)

        # 填充RGB数组
        for i in range(height):
            for j in range(width):
                rgb_data[i, j] = convert_to_rgb(data[i * width + j])

        # 创建图像
        image = Image.fromarray(rgb_data, 'RGB')

        # 保存图像
        output_image_file = f"{screen_name}.png"
        image.save(output_image_file)

        print(f"Image saved as {output_image_file}")

if __name__ == "__main__":
    main()
