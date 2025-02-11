# Instructions

## Introduction
This documentation explains how to use the `cou_screen.py` program to decode the images in the `.h` files located in the `src/media/` folder and place the decoded images into the `img` folder. The program is located in the `img` folder.

## Prerequisites
Before running `cou_screen.py`, please ensure that Python is installed in your environment and that you have downloaded the `cou_screen.py` script.

## Steps to Use

1. **Navigate to the working directory**:
    Open the terminal and navigate to the working directory containing the `cou_screen.py` script. For example:
    ```sh
    cd /NerdMiner_v2/
    ```

2. **Run the script**:
    Run the `cou_screen.py` script using the following command:
    ```sh
    python cou_screen.py src/media/images_320_170.h
    ```

3. **Check the output**:
    After running the script, the decoded images will be saved in the `img` folder. You can view the generated image files in that folder.

## Notes
- The `src/media/` folder contains model files adapted for different resolution hardware. The file suffix indicates the screen resolution.

After localizing the images, `image_to_header.py` performs the reverse operation, converting the PNG files back into the corresponding `.h` files. 使用说明

## 简介
本说明文档介绍了如何使用 `cou_screen.py` 程序来解开 `src/media/` 文件夹下 `.h` 文件中的取模图片，并将解开的图片放到 `img` 文件夹下。程序在img文件夹下。

## 前提条件
在运行 `cou_screen.py` 之前，请确保您的环境中已经安装了 Python，并且已经下载了 `cou_screen.py` 脚本。

## 使用步骤

1. **导航到工作目录**：
    打开终端并导航到包含 `cou_screen.py` 脚本的工作目录。例如：
    ```sh
    cd /NerdMiner_v2/
    ```

2. **运行脚本**：
    使用以下命令运行 `cou_screen.py` 脚本：
    ```sh
    python cou_screen.py src/media/images_320_170.h
    ```

3. **查看输出**：
    脚本运行后，解开的图片将会被保存到 `img` 文件夹中。您可以在该文件夹中查看生成的图片文件。

## 注意事项
-  `src/media/` 会有适配不同分辨率硬件的模型文件。文件后缀为屏幕的分辨率。

后续汉化图片后，image_to_header.py是反向操作，即把png文件转换成对应的.h文件
