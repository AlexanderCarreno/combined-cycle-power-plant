# Combined Cycle Power Plant project

## Machine learning selecion

In this project we need to predict a target value and also the excercise has data available, thats why i select *Supervised learning - regressio*

## Algorithm selection

For the example described in this problem i select two algorithms to work with, *Ridge regression* and *Lasso regression*

## Observations comparing algorithms

### Params defined

Below are the params used in the models, for those two i use the same params, in this excersie i use the the cross-validation n-k method to train different models, the best model was choosed taking into account the average of the mean squared errors (taking the most closed below)

#### Glosarry

- Temperature (T)
- Exhaust Vacuum (V)
- Ambient Pressure (AP)
- Relative Humidity (RH)
- Net hourly electrical energy output (PE) __Feature to predict__

### Observations and results

| Algorithm | Features removed | Alpha | MSE Average (5) | MSE Best model | MAPE Best Model |
| :---              |:----:|:----:|:----:|:----:| ---: |
| Lasso  regression | None | 1 | 20.85 | 20.06 | 0.79% |
| Ridge regression  | None | 1 | 20.79 | 19.90 | 0.79% |
| Lasso  regression | T | 1 | 57.15 | 56.64 | 1.29% |
| Ridge regression  | T | 1 | 57.12 | 56.60 | 1.29% |
| Lasso  regression | V | 1 | 23.08 | 22.01 | 0.82% |
| Ridge  regression | V | 1 | 23.03 | 21.86 | 0.82% |
| Lasso  regression | AP | 1 | 20.94 | 20.14 | 0.79% |
| Ridge  regression | AP | 1 | 20.88 | 19.98 | 0.78% |
| Lasso  regression | RH | 1 | 23.94 | 23.85 | 0.85% |
| Ridge  regression | RH | 1 | 23.91 | 23.82 | 0.85% |

The best results in this case is to use all the features available to fit the model and then make predictions, taking into account that the most important feature is Temperature in our model, also we can notice that Ridge regression has the best performance in this task

Now changing the hyperparameters, please see results above

| Algorithm | Features removed | Alpha | MSE Average (5) | MSE Best model | MAPE Best Model |
| :---              |:----:|:----:|:----:|:----:| ---: |
| Lasso  regression | None | 1 | 20.85 | 20.06 | 0.79% |
| Ridge regression  | None | 1 | 20.79 | 19.90 | 0.79% |
| Lasso  regression | None | 0.5 | 20.81 | 19.96 | 0.79% |
| Ridge regression  | None | 0.5 | 20.79 | 19.90 | 0.79% |
| Lasso  regression | None | 0.2 | 20.79 | 19.92 | 0.79% |
| Ridge regression  | None | 0.2 | 20.79 | 19.90 | 0.79% |
| Lasso  regression | None | 0.01 | 20.79 | 19.90 | 0.79% |
| Ridge regression  | None | 0.01 | 20.79 | 19.90 | 0.79% |

We can notice here that  Lasso regression can be improve if you compare it with Ridge regression, however Ridge regression sill has better performance in this problem, so the best model to resolve it is Ridge regression

by Alexander Carreño Correa
