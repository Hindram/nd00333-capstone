import joblib
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.core import Workspace, Dataset


run = Run.get_context()
ws = run.experiment.workspace

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--data', type=str, help="Loading dataset")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()
    
    # split data to train and test sets
    dataset = Dataset.get_by_name(ws, name='diabetes_data_set')
    dataset = dataset.to_pandas_dataframe()
    x = dataset.drop(columns=['Overcome'])
    y = dataset['Overcome']
    model = Ridge().fit(x,y)
    joblib.dump(model, 'skmodel.pkl')
    run.log("Accuracy", np.float(accuracy))
    
if __name__ == '__main__':
    main()    
