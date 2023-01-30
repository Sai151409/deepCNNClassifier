from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallBackModel, TrainingModel
from deepClassifier import logger

STAGE_NAME = 'Training Stage'


def main():
    config = ConfigurationManager()
    training_config = config.get_training_config()
    prepare_callbacks_config = config.get_prepare_callback_config
    prepare_callbacks = PrepareCallBackModel(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

    training = TrainingModel(config=training)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list=callback_list)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
