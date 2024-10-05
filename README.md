# Image Classification Model using TensorFlow

## Overview

This project is an image classification application built using **TensorFlow**. It uses a **Convolutional Neural Network (CNN)** to classify images into two categories. The model was developed using **TensorFlow 2.11** and includes several **Dropout** layers to prevent overfitting.

### Features

- **Convolutional Neural Network (CNN)**: A CNN architecture designed to classify images.
- **Binary Classification**: The model classifies images into two classes.
- **Dropout Layers**: Used to reduce overfitting and improve model generalization.
- **Customizable Image Shape**: The input image size is customizable using `image_dataset_from_directory`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/).
- **TensorFlow**: You need TensorFlow 2.11 (with GPU support) to run the model efficiently.

Install the necessary dependencies:

```bash
pip install tensorflow-gpu==2.11.0
pip install opencv-python
pip install matplotlib
