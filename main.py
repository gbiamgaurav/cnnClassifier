
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_training import ModelTrainingPipeline
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e 
    

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    raise e