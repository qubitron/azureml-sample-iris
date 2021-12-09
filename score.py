import json
import numpy as np
import os
import joblib
import mlflow

def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model")
    model = mlflow.pyfunc.load_model(model_path)


def run(raw_data):
    result = model.predict(json.loads(raw_data)["input_data"]["data"])
    return result.tolist()
