import json
import pickle
import numpy as np
import pandas as pd
import os
import joblib
from azureml.core.model import Model

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


def init():
    global model
    # Replace filename if needed.
    path = os.getenv('AZUREML_MODEL_DIR') 
    model_path = os.path.join(path, 'model.joblib')
    # Deserialize the model file back into a sklearn model.
    model = joblib.load(model_path)


input_sample = pd.DataFrame(data = [{"Pregnancies": 6, 
 "Glucose": 148, 
 "BloodPressure": 72, 
 "SkinThickness": 35, 
 "Insulin": 0, 
 "BMI": 33.5, 
 "DiabetesPedigreeFunction": 0.627, 
 "Age": 50},
        
{"Pregnancies": 1, 
 "Glucose": 85, 
 "BloodPressure": 66, 
 "SkinThickness": 29, 
 "Insulin": 20, 
 "BMI": 26.5, 
 "DiabetesPedigreeFunction": 0.351, 
 "Age": 31}])

# This is an integer type sample. Use the data type that reflects the expected result.
output_sample = np.array([0, 1])

# To indicate that we support a variable length of data input,
# set enforce_shape=False
@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        print("input_data....")
        print(data.columns)
        print(type(data))
        result = model.predict(data)
        print("result.....")
        print(result)
    # You can return any data type, as long as it can be serialized by JSON.
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
