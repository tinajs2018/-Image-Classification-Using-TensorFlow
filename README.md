# Image Classification Using TensorFlow

## Overview

This project aims to classify images into their respective categories using TensorFlow. The dataset used is CIFAR-10, which contains 60,000 images from 10 different categories. We build a baseline image classification model and optimize it using transfer learning with a pre-trained model.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data
   cd image-classification-tensorflow



project/
│
├── app/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── __init__.py
│   ├── app.py
│   └── utils.py
│
├── data/
│   ├── data_loading.py
│   └── preprocessing.py
│
├── models/
│   ├── baseline_model.py
│   ├── transfer_learning_model.py
│   └── train.py
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Baseline_Model.ipynb
│   └── Transfer_Learning.ipynb
│
├── reports/
│   ├── baseline_model_report.md
│   └── transfer_learning_report.md
│
├── image_classification_model.h5
├── requirements.txt
└── README.md
