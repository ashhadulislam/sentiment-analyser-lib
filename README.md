[![PyPI version](https://badge.fury.io/py/sentimentanalyser.svg)](https://badge.fury.io/py/sentimentanalyser)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HitCount](http://hits.dwyl.io/ashhadulislam/sentiment-analyser-lib.svg)](http://hits.dwyl.io/ashhadulislam/sentiment-analyser-lib)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sentimentanalyser.svg)](https://img.shields.io/pypi/dm/sentimentanalyser.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ashhadulislam/sentiment-analyser-lib/badge/master)](https://www.codefactor.io/repository/github/ashhadulislam/sentiment-analyser-lib/overview/master)
# sentiment-analyser-lib

### Installation
Use below command to use install 
`pip install sentimentanalyser`

### Usage
New version Supports the following libraries:

1. Nearest Neighbors
2. Linear SVM
3. RBF SVM 
4. Decision Tree
5. Random Forest
6. Neural Net
7. Naive Bayes

For training the model

Provide the file path where data is available
```
from sentimentanalyser import model_train

# Path to training data and output
filePath="/path_to_data/twitter_train.csv"
outputDir="/path_to_output/outputs"

trainObj=model_train.Train()
trainObj.train_file_model(filePath,outputDir)
```
##### For test data
```
from sentimentanalyser import model_test
testText=""
test_file_name="/path_to_testdata/twitter_test.csv"
test_reference_file="twitter_train"
outputDir="/path_to_output/outputs"
testObj=model_test.TestData()

testedDataFrame=testObj.test_model(testText,test_file_name,test_reference_file,outputDir)
```
