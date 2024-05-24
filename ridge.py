import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

from src.evaluation import model_evaluation
from src.prediction import prediction_example

print('\n===================================================')
print('=============== Ridge Regresion ================== ')
print('===================================================\n')


# 2) Data understanding
# The columns in the data consist of hourly average ambient variables:
# - Temperature (T) in the range 1.81°C to 37.11°C,
# - Exhaust Vacuum (V) in the range 25.36-81.56 cm Hg
# - Ambient Pressure (AP) in the range 992.89-1033.30 milibar,
# - Relative Humidity (RH) in the range 25.56% to 100.16%
# - Net hourly electrical energy output (PE) 420.26-495.76 MW (Target we are trying to predict)
# CCPP means combined-cycle-power-plant
df_CCPP = pd.read_csv('resources/CCPP_data.csv')


# 3) Data Preparation
df_CCPP = df_CCPP.rename({'AT': 'T'}, axis=1)
x = df_CCPP[['T', 'V', 'AP', 'RH']]
y = df_CCPP['PE']


# 4) Modeling
alpha = 1.0
model = Ridge(alpha) 
kfold = KFold(n_splits=5)

mean_squared_errors = []
mean_absolute_percentage_errors = []
models = []
x = x.to_numpy()
for train_index, test_index in kfold.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mean_absolute_percentage_errors.append(mape*100)
    mean_squared_errors.append(mse)
    models.append(model)

# 5) Evaluation
model_evaluation(alpha, mean_squared_errors, mean_absolute_percentage_errors)

# 6) Deployment
prediction_example(models[0])