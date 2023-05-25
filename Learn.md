## Learn.md

# Automated Algebraic Equation Generation And Evaluation From Sinhala Math Word Problems

## Introduction
This repository contains a system that solves simple algebraic equations and classifies the types of simultaneous equations. It preprocesses questions and maps numerical values to equations, providing the output answer. The classification of simultaneous equations is done using two approaches: the Dynamic approach and the rule-based approach. The rule-based approach maps values extracted from the questions to a template based on a defined set of rules, while the Dynamic approach uses an ANN model for equation classification.

## Approach
### Preprocessing 
The preprocessing step involves preparing the input data by converting it into a suitable format for equation generation and evaluation.

![Preprocessing](https://github.com/Chamindu36/AUTOMATED-ALGEBRIC-EQUATION-GENERATION-AND-EVALUATION-FROM-SINHALA-MATH-WORD-PROBLEMS/blob/master/Screen%20Shot%202022-02-22%20at%203.00.01%20PM.png?raw=true)

### Equation Generator and Equation Solver
The equation generator and solver components are responsible for generating algebraic equations based on the preprocessed input and solving them to obtain the desired output.

![Equation Generator and Solver](https://github.com/Chamindu36/AUTOMATED-ALGEBRIC-EQUATION-GENERATION-AND-EVALUATION-FROM-SINHALA-MATH-WORD-PROBLEMS/blob/master/Screen%20Shot%202022-02-22%20at%202.59.41%20PM.png?raw=true)

## Setup Instructions for Windows
1. Follow the steps mentioned in [this Colab notebook](https://colab.research.google.com/drive/179ypZund7SiDDw0Sq_O_Eq_qVr_uRrJ-?usp=sharing) to obtain the required Python packages.
2. Install Nvidia CUDA 2.X version.
3. Install NLTK 3.2.5 using the following command:
```
pip install nltk==3.2.5
```
4. Install TensorFlow 2.0.0 and Keras 2.3.1 using the following commands:
```
pip install tensorflow==2.0.0
pip install keras==2.3.1
```
5. Install scikit-learn 0.22.2 and NumPy 1.18.1 using the following commands:
```
pip install scikit-learn==0.22.2
pip install numpy==1.18.1
```
6. Clone this repository to your local machine.
7. Update the main path in the code to match your local setup.
8. Build the Python project.
9. Install the given dependencies.

## Running the Tool on Windows
1. Wait until the GUI appears.
2. Check the samples provided in the Testing folder and create your question. Paste the question into a text file.
3. Check the radio button to indicate whether the question is a simple one or a complex one.
4. Upload the text file with the created question.

![Tool GUI](/2a490c97-e1da-413a-a53f-8dba6ccda6ce.jpg?raw=true)

Note: Please ensure that you have followed all the setup instructions properly before running the tool.
