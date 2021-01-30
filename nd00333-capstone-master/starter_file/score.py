# Source: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model

import json
import os
import joblib
import pandas as pd
import numpy as np


def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    model = joblib.load(model_path)

def run(data):
    try:      
        data = json.loads(data)['data']
        data = pd.DataFrame.from_dict(data)
        result = model.predict(data)
        
        return result.tolist()

    except Exception as e:
        error = str(e)
        return error
