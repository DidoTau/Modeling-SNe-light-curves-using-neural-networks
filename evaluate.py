# Created by E. Ramírez 
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Evaluate(object):
  """ 
  Evaluates a neural network model
  """
  def __init__(self,model,X_test, y_test):

    """Initialize an instance to evaluate a given model based on 
    a given test set

    Args:
    model ([type]): [description]
    X_test ([type]): [description]
    y_test ([type]): [description]
    """
    self.model = model
    self.X_test = X_test
    self.y_test = y_test
 
  def residual(self,t_min, t_max, ntimes):
    """Generates residual vectors 
    Args:
        t_min ([type]): [description]
        t_max ([type]): [description]
        ntimes ([type]): [description]

    Returns:
        3-tuple: [description]
    """
    df_test_params = pd.DataFrame(self.X_test[:,:-1,0])
    times = np.logspace(np.log10(t_min), np.log10(t_max), ntimes)
    scale_t = MinMaxScaler()
    scaled_time = scale_t.fit(times.reshape(-1, 1))
    X_test_inv = scale_t.inverse_transform(self.X_test[:,-1])
    y_pred = self.model.predict(self.X_test)
    
    df_pred = pd.DataFrame(y_pred[:,0,0], index = X_test_inv[:,0], columns =['magnitud'] )
    df_test = pd.DataFrame(self.y_test,index = X_test_inv[:,0], columns =['magnitud'] )
    df_res = np.abs(df_pred- df_test)
    index = np.sort(df_res.index.unique().values)

    y_res = []
    y_low = []
    y_upp = []
    for i in index:
      res = df_res.loc[i]
      y_res.append(res.mean())
      y_low.append(res.quantile(0.16)[0])
      y_upp.append(res.quantile(0.84)[0])
    return index,y_res, [y_low, y_upp]
