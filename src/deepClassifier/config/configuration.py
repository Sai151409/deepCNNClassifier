from deepClassifier.utils import read_yaml_file, create_directories
from deepClassifier.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig, \
    PrepareCallBackConfig, TrainingConfig, EvaluationConfig
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_classes=self.params.CLASSES,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS
        )

        return prepare_base_model_config
    
    
    def get_prepare_callback_config(self) -> PrepareCallBackConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_file_path)
        create_directories([Path(model_ckpt_dir), Path(config.tensorboard_root_log_dir)])

        prepare_callbacks_config = PrepareCallBackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_file_path=Path(config.checkpoint_model_file_path)
        )
        return prepare_callbacks_config
    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "PetImages")
        create_directories([training.root_dir])
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_batch_size=params.BATCH,
            params_epochs=params.EPOCHS,
            params_image_size=params.IMAGE_SIZE,
            params_is_augmentation=params.AUGMENTATION
            )
        return training_config
    
    
    def get_evaluation_config(self)->EvaluationConfig:
        evaluation_config = EvaluationConfig(
            model_path=self.config.training.trained_model_path,
            training_data=self.config.data_ingestion.unzip_dir,
            all_params=self.params,
            image_size = self.params.IMAGE_SIZE,
            batch_size = self.params.BATCH
        )
        return evaluation_config
