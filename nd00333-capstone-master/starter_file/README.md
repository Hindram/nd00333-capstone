
# Capstone Project: Diabetes prediction

The used dataset originally has been taken from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the project is to predict if a patient has diabetes or not by evaluating certain diagnostic measurements. 

## Project Set Up and Installation

To run the project, follow the steps below:

- Upload notebooks to the AzureML workspace.
- Create a new compute instance to run the notebook script, STANDARD_DS2_V12 was selected.
- Create a cpu compute cluster of type STANDARD_DS12_V2 with 4 max nodes, and low priority status to train the model.
- Registered Kaggle dataset to the workspace under the name "diabetes_data_set", and retrieved it later in the ML experiment.

- Run the AutoML experiment through 'automl.ipynb' notebook as follow: 
  - Load the ws, dataset, compute cluster.
  - Create a new experiment named 'automl-exp'.
  - Add the AutoML settings and configuration information, then submit the experiment to train the model.
  - Use the RunDetails widget to show experiment details such as the runs accuracy rate.
  - Retrive the best model and registerd it in the workspace.
  - Deploy the best model as a web service using Inference & deployment configuration settings. 
  - Test the endpoint by sending json payload and receive a response.
  - Enable the application insights and service logs.

- Run the HyperDrive experiment through 'hyperparameter_tuning.ipynb' notebook as follow: 
  - Load the ws, dataset, compute cluster.
  - Create a new experiment named 'hyperdrive_exp'.
  - Define early termination policy, Random Parameter Sampling  hyperparmenter and config settings. 
  - Create 'train.py' script to be used in training the model, then submit the experiment.
  - Use the RunDetails widget to show experiment details such as the runs accuracy rate.

## Dataset

### Overview
The dataset collects the records of females patients of age 21 and older from Pima Indian heritage. The dataset has a total of 768 entries. The objective is to predict if a patient has diabetes or not by evaluating certain diagnostic measurements.
https://www.kaggle.com/mathchi/diabetes-data-set

### Task
Predict the "Outcome" column based on the input features, either the patient has diabetes or not. 

The dataset has nine features as follow:
- Pregnancies: Number pregnancy times (int).
- Glucose: Plasma glucose concentration level (int). 
- BloodPressure: Diastolic blood pressure level in mm Hg(int).
- SkinThickness: skinfold thickness in mm(int).
- Insulin: two-hour serum insulin measured by mu U/ml(int).
- BMI: Body mass index (float).
- DiabetesPedigreeFunction: Diabetes pedigree function(float).
- Age: age in years 21 and above(int).
- Outcome: Target column 0 or 1, 0 = Not diabetes, 1 = diabetes(int).

### Access
The data is registered in the AzureML workspace as a dataset with the name 'diabetes_data_set'. Then, used in both notebooks using Python SDK.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
- Udacity Nanodegree Content.
- https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-power-bi-custom-model
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-environments
- https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-bring-data
- https://docs.microsoft.com/en-us/azure/machine-learning/resource-curated-environments
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=python#define-an-entry-script
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-enable-app-insights

