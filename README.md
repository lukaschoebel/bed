# bed - Bark Beetle Detection

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Objective](#objective)
- [Pipeline](#pipeline)
- [Get Started](#get-started)
- [Frameworks](#frameworks)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Objective

The overall objective of this project is to be able to differentiate different sounds in audio files. In the end we want to be able to detect sounds of bark beetles in trees.

## Pipeline

0. Read Audio Files
1. Audio Data PreProcessing (Filtering?)
2. Audio Processing & Evaluation (🐛 or 🚫)
3. Final Decision

## Get Started

- Install [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Create Virtual environment with `conda create -n <ENV_NAME> python=3.6`
- Activate venv with `conda activate <ENV_NAME>`
- Install requirements with `pip install -r requirements.txt`
- Removing venv by first deactivataing and then `conda env remove -n <ENV_NAME>`

## Key Insights on Evaluation


## Papers & Resources & Interesting Things

- [**Acoustic Detection and Identification of Insects in Soil**](https://www.ars.usda.gov/ARSUserFiles/3559/publications/685_1.pdf) by Mankin et. Al. (1998)
- [**Think DSP**](http://greenteapress.com/thinkdsp/thinkdsp.pdf) by Allen Downey (2014)
- [**Automatic acoustic detection of birds through deep learning**](https://arxiv.org/pdf/1807.05812.pdf) by Stowell et. Al. (2018)

## Acknowledgements

- kudos to **Kartik Chaudhary** and his [spectrogram.py](https://gist.github.com/kartikgill/a1a6efdac872a9e66d528b93eb049f74)