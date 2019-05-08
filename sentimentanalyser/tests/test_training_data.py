from unittest import TestCase

from ..model_train import Train


class TestTrain(TestCase):
	def test_training_data(self):
		file_path = input('Enter the filePath of the training data')
		output_dir = input('Enter the outputDir to generate trained models')
		objTrain = Train()
		s = objTrain.train_file_model(file_path, output_dir)
		# self.assertTrue(isinstance(s, basestring))
