# deep Classifier Project

## workflow

1. update config.yaml   
2. update secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. test run pipeline
9. run tox for testing your package
10. update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline 


MLFLOW_TRACKING_URI=https://dagshub.com/Sai151409/deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=Sai151409 \
MLFLOW_TRACKING_PASSWORD=73519799ff6a90796c3135ea60eadecd40df0823  \
python script.py