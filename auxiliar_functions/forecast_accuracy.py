import numpy as np
import pandas as pd

# Accuracy metrics
def forecast_accuracy(forecast, actual):
    mae = round(np.mean(np.abs(forecast - actual)), 2)  # MAE
    mse = round(np.mean(np.square(forecast - actual)), 2)  # MSE
    mape = round(np.mean(np.abs(forecast - actual)/np.abs(actual)), 2)  # MAPE
    rmse = round(np.sqrt(np.mean(np.square(forecast - actual))), 2)  # RMSE
    
    scores = pd.DataFrame([mae,mse,mape,rmse], index=['MAE','MSE','MAPE','RMSE'], columns=['Scores'])
    
    return scores
