import tensorflow as tf
from deepClassifier.entity import EvaluationConfig
from pathlib import Path
from deepClassifier.utils.common import create_directories, save_json


class EvaluationModel:
    def __init__(self,
                 config: EvaluationConfig):
        self.config = config
        
    def _test_data(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30)
        dataflow_kwargs = dict(
            target_size = self.config.image_size[:-1],
            batch_size = self.config.batch_size,
            interpolation='bilinear'
        )
        
        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.test_data = test_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )
    
    @staticmethod
    def load_model(path: Path)-> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        model = self.load_model(path=self.config.model_path)
        self._test_data()
        self.score = model.evaluate(self.test_data)
        
    def save_score(self):
        scores = {"loss" : self.score[0], "accuracy" : self.score[1]}
        save_json(path=Path("scores.json"), data=scores)