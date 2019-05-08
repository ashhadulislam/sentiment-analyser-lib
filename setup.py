from setuptools import setup

setup(
      name='sentimentanalyser',
      version='2.5',
      description='Generic python library to perform sentiment analysis on any dataset, using different models',
      long_description='A generic package to help developers perform analysis on their dataset, powered by Nearest '
                       'Neighbors, Linear SVM, RBF SVM, Decision Tree,Random Forest, Neural Net and Naive-Bayes '
                       'models.',
      url='',
      author='Sanjay Pradeep,Jayanth Anantharapu, Aditya Kumar, Ashhadul Islam',
      author_email='sanjay.sndk@gmail.com, aditya00kumar@gmail.com, ashhadulislam@gmail.com',
      keywords='Classification, Binary Classification, Multi-label Classification, Text data',
      license='MIT',
      packages=['sentimentanalyser'],
      install_requires=[
            "nltk",
            "numpy",
            "openpyxl",
            "pandas",
            "scikit-learn",
            "scipy",
            "six",
            'tqdm'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False
)
