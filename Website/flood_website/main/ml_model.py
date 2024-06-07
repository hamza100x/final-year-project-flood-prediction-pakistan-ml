import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pickle

def Temp_q(pro,inp):
	if(pro==1):
		model = pickle.load(open(r'main\static\main\assets\PKL\P_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==2):
		model = pickle.load(open(r'main\static\main\assets\PKL\S_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==3):
		model = pickle.load(open(r'main\static\main\assets\PKL\K_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==4):
		model = pickle.load(open(r'main\static\main\assets\PKL\B_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==5):
		model = pickle.load(open(r'main\static\main\assets\PKL\G_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==6):
		model = pickle.load(open(r'main\static\main\assets\PKL\F_Temp_rf.sav', 'rb'))
		pred =model.predict(inp)
	return pred


def Veg_q(pro,inp):
	if(pro==1):
		model = pickle.load(open(r'main\static\main\assets\PKL\P_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==2):
		model = pickle.load(open(r'main\static\main\assets\PKL\S_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==3):
		model = pickle.load(open(r'main\static\main\assets\PKL\K_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==4):
		model = pickle.load(open(r'main\static\main\assets\PKL\B_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==5):
		model = pickle.load(open(r'main\static\main\assets\PKL\G_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==6):
		model = pickle.load(open(r'main\static\main\assets\PKL\F_Veg_rf.sav', 'rb'))
		pred =model.predict(inp)
	return pred


def Ndsi_q(pro,inp):
	if(pro==1):
		model = pickle.load(open(r'main\static\main\assets\PKL\P_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==2):
		model = pickle.load(open(r'main\static\main\assets\PKL\S_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==3):
		model = pickle.load(open(r'main\static\main\assets\PKL\K_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==4):
		model = pickle.load(open(r'main\static\main\assets\PKL\B_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==5):
		model = pickle.load(open(r'main\static\main\assets\PKL\G_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==6):
		model = pickle.load(open(r'main\static\main\assets\PKL\F_Ndsi_rf.sav', 'rb'))
		pred =model.predict(inp)
	return pred


def Rain_q(pro,inp):
	if(pro==1):
		model = pickle.load(open(r'main\static\main\assets\PKL\P_Rain_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==2):
		model = pickle.load(open(r'main\static\main\assets\PKL\S_Rain_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==3):
		model = pickle.load(open(r'main\static\main\assets\PKL\K_Rain_lr.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==4):
		model = pickle.load(open(r'main\static\main\assets\PKL\B_Rain_lr.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==5):
		model = pickle.load(open(r'main\static\main\assets\PKL\G_Rain_rf.sav', 'rb'))
		pred =model.predict(inp)
	elif(pro==6):
		model = pickle.load(open(r'main\static\main\assets\PKL\F_Rain_rf.sav', 'rb'))
		pred =model.predict(inp)
	return pred
