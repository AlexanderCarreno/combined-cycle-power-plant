import numpy as np

def render_prediction(
        prediction, 
        features):

    print(f'Parametrs: temperature:{features[0][0]}, exhaust_vacuum:{features[0][1]}, ambient_pressure:{features[0][2]}, relative_humidity:{features[0][3]}')
    print(f'Net hourly electrical energy output (PE): {prediction}\n')

def prediction_example(model):
    temperature = 14.96
    exhaust_vacuum = 41.76
    ambient_pressure = 1024.07
    relative_humidity = 73.17

    features = np.array([[temperature, exhaust_vacuum, ambient_pressure, relative_humidity]])
    prediction = model.predict(features)
    render_prediction(prediction[0], features)