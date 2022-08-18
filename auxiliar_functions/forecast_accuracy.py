import numpy as np

# Accuracy metrics
def forecast_accuracy(forecast, actual):
    mae = np.mean(np.abs(forecast - actual))  # MAE
    mse = np.mean(np.square(forecast - actual))  # MSE
    mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
    rmse = np.sqrt(np.mean(np.square(forecast - actual)))  # RMSE
    
    return({'mae':mae, 'mse':mse, 'mape':mape, 'rmse':rmse})
