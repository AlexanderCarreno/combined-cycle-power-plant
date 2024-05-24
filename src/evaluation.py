import numpy as np

def model_evaluation(alpha, 
                     mean_squared_errors, 
                     mean_absolute_percentage_errors):
    print(f'Alpha value in this model {alpha}\n')
    print(f'Scores mean_squared_errors: {mean_squared_errors}')
    print(f'MSE Cross-validation average: {np.mean(mean_squared_errors)}\n')
    print(f'Scores mean_absolute_percentage_errors: {mean_absolute_percentage_errors}\n')