# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:47:02 2022

@author: crist
"""
# librerias
import pandas as pd
import numpy as np
import os
import re

def valores_nulos_df(df):
	"""
	Calcula el total y porcentaje de los valores nulos de un dataframe.
	Lo que devuelve es otro dataframe con esta informacion.
	"""
	df_null = pd.DataFrame([df.isnull().sum(),round(df.isnull().sum()/len(df),2)]).transpose()
	df_null.columns = ['Total','Porcentaje']
	df_null = df_null.sort_values(by='Total', ascending=False)
	df_null
	
	return df_null