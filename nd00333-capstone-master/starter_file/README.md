
# Capstone Project: Diabetes prediction

The used dataset originally has been taken from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the project is to predict if a patient has diabetes or not by evaluating certain diagnostic measurements. 

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The dataset collects the records of females patients of age 21 and older from Pima Indian heritage. The dataset has a total of 768 entries. The objective is to predict if a patient has diabetes or not by evaluating certain diagnostic measurements.
https://www.kaggle.com/mathchi/diabetes-data-set

### Task
Predict the "Outcome" column based on the input features, either the patent has diabetes or not. 

The dataset has nine features as follow:
Pregnancies: Number pregnancy times (int).
Glucose: Plasma glucose concentration level (int). 
BloodPressure: Diastolic blood pressure level in mm Hg(int).
SkinThickness: skinfold thickness in mm(int).
Insulin: two-hour serum insulin measured by mu U/ml(int).
BMI: Body mass index (float).
DiabetesPedigreeFunction: Diabetes pedigree function(float).
Age: age in years 21 and above(int).
Outcome: Target column 0 or 1 (int)

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
