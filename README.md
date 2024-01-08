# Quick demo available at: [HF spaces](https://huggingface.co/spaces/fubuki119/JokesGPT)

# JokesGPT
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/VaruN-dev-dev/JestGenius?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/VaruN-dev-dev/JestGenius)
![GitHub pull requests](https://img.shields.io/github/issues-pr/VaruN-dev-dev/JestGenius)
![GitHub](https://img.shields.io/github/license/VaruN-dev-dev/Machine-Translation)
![contributors](https://img.shields.io/github/contributors/VaruN-dev-dev/JestGenius)
![codesize](https://img.shields.io/github/languages/code-size/VaruN-dev-dev/JestGenius)

A Deep learning Model for Jokes Generation.

# Project Overview
## Introduction

This project focuses on generation of Jokes using GPT.
This is a fine-tuned version of [gpt2 model](https://huggingface.co/gpt2), adapted to [jokes dataset](https://huggingface.co/datasets/Amirkid/jokes?row=51)


# Objectives
- To explore the capabilities of gpt2 model

# Installation and Setup
> Clone the Repository
```
git clone https://github.com/VaruN-dev-dev/JestGenius.git
```

> Navigate into the Repository

```
cd JestGenius
```

> Crete a Virtual Environment

```
conda create -p venv
```
> Activate the Virtual Environment

```
conda activate venv/
```

> Install dependencies

```
pip install requirements.txt
```

> Running the Gradio App

```
python app.py
```

## Codes and Resources Used
In this section I give user the necessary information about the software requirements.
- **Editor Used:**  Visual Studio Code
- **Python Version:**  Python 11.0

## Python Packages Used
The project relies on several Python packages, all of which are listed in `requirements.txt.`

# Data
## Source Data/ Data Acquisition
The project utilizes the [jokes dataset](https://huggingface.co/datasets/Amirkid/jokes?row=51) dataset, comprising of English jokes sentences.



# Results and evaluation
To be written..

# Future work
- Enhance and train the model on more data
- Fine tune model using LoRas and QLoras to compare the results.
- To add a training and eval script.

# Acknowledgments/References

> Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya. Language Models are Unsupervised Multitask Learners. 2019

# License
For this github repository, the License used is [MIT License](https://opensource.org/license/mit/).
