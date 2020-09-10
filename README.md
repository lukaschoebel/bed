# bed - Bark Beetle Detection

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Objective](#objective)
- [Pipeline](#pipeline)
- [Get Started](#get-started)
- [Frameworks](#frameworks)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 🚩 Objective

As a binary classification task, the overall objective of this project is to be able to detect sounds from trees and to differentiate between a tree that is infested with bark beetles and one that is not. In the end we want to be able to detect sounds of bark beetles in trees.

## 👾 Pipeline

0. Read Audio Files + Amplification
1. Audio Data PreProcessing (Filtering?)
2. Audio Processing & Evaluation (🐛 or 🚫)
3. Final Decision

## 🎬 Get Started

- Install [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Create Virtual environment with `conda create -n <ENV_NAME> python=3.6`
- Activate venv with `conda activate <ENV_NAME>`
- Install requirements with `pip install -r requirements.txt`
- Removing venv by first deactivataing and then `conda env remove -n <ENV_NAME>`

## 👀 Ideas & Insights on Evaluation

- Use of CNNs/CRNNs/CNN-densenet seems to be interesting, GMMs/PSKs/SVMs secondary
- features based on Mel-spectrogram, low Mel-band energies 
- Data augmentation by adding noise, audio time shift, cropping, freq shift & possibly time reversal
- Model ensembling by averaging?
- (Possibly PCA for dimensionality reduction?)

## 📚 Papers & Resources & Interesting Things

- [**Acoustic Detection and Identification of Insects in Soil**](https://www.ars.usda.gov/ARSUserFiles/3559/publications/685_1.pdf) by Mankin et Al. (1998)
- [**Think DSP**](http://greenteapress.com/thinkdsp/thinkdsp.pdf) by Allen Downey (2014)
- [**Automatic acoustic detection of birds through deep learning**](https://arxiv.org/pdf/1807.05812.pdf) by Stowell et Al. (2018)
- [**Bulbul Bird Detection**](https://github.com/DCASE-REPO/bulbul_bird_detection_dcase2018) with 88.7% h.m.AUC for bird sounds by Thomas Grill et Al. (2018)
- [**An End-to-End Trainable Neural Network for Image-based SequenceRecognition and Its Application to Scene Text Recognition**](https://arxiv.org/pdf/1507.05717.pdf) by Shi et Al. (2015)
- [**CRNN**](https://github.com/meijieru/crnn.pytorch) by Jieru Mei (2019)

## 👏 Acknowledgements

- kudos to **Kartik Chaudhary** and his [spectrogram.py](https://gist.github.com/kartikgill/a1a6efdac872a9e66d528b93eb049f74)