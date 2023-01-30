from deepClassifier.config import ConfigurationManager
from deepClassifier.components import EvaluationModel
from deepClassifier import logger

STAGE_NAME = 'Evaluation Stage'

def main():
    config = ConfigurationManager()
    evaluation_config = config.get_evaluation_config()
    evaluation = EvaluationModel(config=evaluation_config)
    evaluation.evaluation()
    evaluation.save_score()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e