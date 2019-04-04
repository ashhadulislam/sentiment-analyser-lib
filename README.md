# sentiment-analyser-lib

### Installation
Use below command to use install 
`pip install sentimentanalyser`

### Usage

For training the model
`from sentimentanalyser import train`
Provide the file path where data is available

```filePath="/path_to_data/twitter_train.csv"

outputDir="/path_to_output/outputs"

trainObj=train.Train()

trainObj.train_file_model(filePath,outputDir)```

For test data

`from sentimentanalyser import test

testText=""

test_file_name="/Users/amirulislam/Desktop/testing_datasets/twitter_test.csv"

test_reference_file="twitter_train"

outputDir="/Users/amirulislam/Desktop/outputs"

testObj=test.TestData()

testedDataFrame=testObj.test_model(testText,test_file_name,test_reference_file,outputDir)`

from sentimentanalyser import test

testText=""

test_file_name="/Users/amirulislam/Desktop/testing_datasets/bbc_test.csv"

test_reference_file="bbc_train"

outputDir="/Users/amirulislam/Desktop/outputs"

testObj=test.TestData()

testedDataFrame=testObj.test_model(testText,test_file_name,test_reference_file,outputDir)`
Utilization of package in Django application

Go to project feedprocessor

Run: python manage.py runserver

Upload training dataset at

http://localhost:8000/sentiment/models/train/

Then test with your dataset at

http://localhost:8000/sentiment/models/test/
