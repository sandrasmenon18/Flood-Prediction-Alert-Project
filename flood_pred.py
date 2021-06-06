#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv('dist2.csv')
Q1_r=data.Rainfall.quantile(0.25)
Q3_r=data.Rainfall.quantile(0.75)
IQR_r=Q3_r-Q1_r
lower_lim_r=Q1_r-1.5*IQR_r
upper_lim_r=Q3_r+1.5*IQR_r
data=data[(data.Rainfall>lower_lim_r) & (data.Rainfall<upper_lim_r)]
Q1_s=data.Soil_Moisture.quantile(0.25)
Q3_s=data.Soil_Moisture.quantile(0.75)
IQR_s=Q3_s-Q1_s
lower_lim_s=Q1_s-1.5*IQR_s
upper_lim_s=Q3_s+1.5*IQR_s
data=data[(data.Soil_Moisture>lower_lim_s) & (data.Soil_Moisture<upper_lim_s)]
Q1_e=data.Evapo_Transpiration.quantile(0.25)
Q3_e=data.Evapo_Transpiration.quantile(0.75)
IQR_e=Q3_e-Q1_e
lower_lim_e=Q1_e-1.5*IQR_e
upper_lim_e=Q3_e+1.5*IQR_e
dataset=data[(data.Evapo_Transpiration>lower_lim_e) & (data.Evapo_Transpiration<upper_lim_e)]
data = np.array(data)

X = data[:, 1:4]
y = data[:, -1]
y = y.astype('float')
X = X.astype('float')
y = y.reshape(len(y),1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# print(X,y)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(bootstrap=True,
 max_depth=90,
 max_features='sqrt',
 min_samples_leaf= 4,
 min_samples_split=10,
 n_estimators= 400)
regressor.fit(X, y)



inputt=[float(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]

b = regressor.predict(final)


pickle.dump(regressor,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


