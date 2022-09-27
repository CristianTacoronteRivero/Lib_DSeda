# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:47:02 2022

@author: crist
"""
# librerias
import pandas as pd
import numpy as np


def valores_nulos_df(df, solo_nulos=True, grafica=True):
	"""Pasado un DataFrame, se encarga de crear una tabla donde muestra
	los features que tienen valores nulos

	Args:
		df (DataFrame): DataFrame que se desea analizar
		solo_nulos (bool, optional): Muestra solo los features que contienen nulos. Defaults to True.
		grafica (bool, optional): Devuelve una representacion grafica de los valores nulos del DataFrame. Defaults to True.

	Returns:
		Dataframe: Se devuelve un DataFrame que contiene los valores nulos del DataFrame introducido-
	"""
	df_null = pd.DataFrame([df.isnull().sum(),round(df.isnull().sum()/len(df),2)]).transpose()
	df_null.columns = ['Total','Porcentaje']
	df_null = df_null.sort_values(by='Total', ascending=False)

	if solo_nulos:
		df_null = df_null[df_null.Porcentaje>0]

	if grafica:
		pass

	return df_null


from sklearn.base import BaseEstimator, TransformerMixin
class ColumnSelector(BaseEstimator, TransformerMixin):
	"""Clase encargada de ajustarse a un DataFrame introducido y asi devolver los features
	de una determinada naturaleza
	"""

	def __init__(self, dtype):
		self.dtype = dtype

	def fit(self, X, y=None):# comprueba si el objeto es de un tipo de dato especifico, en este caso dataframe
		X = X if isinstance(X, pd.DataFrame) else pd.DataFrame(X)
		if self.dtype == 'numerical':  # si lo que quiero es identificar datos numericos entro aqui
			self.cols = X.select_dtypes(include='number').columns.tolist()
		elif self.dtype == 'categorical': # selecciono columnas de strings
			self.cols = X.select_dtypes(include='object').columns.tolist()
		elif self.dtype == 'datetime':
			self.cols = X.select_dtypes(include='datetime').columns.tolist()

		self.col_idx = [df.columns.get_loc(col) for col in self.cols]
		return self

	def transform(self, X):
		X = X.values if isinstance(X, pd.DataFrame) else X
		return X[:, self.col_idx]

if __name__ == '__main__':
	df = pd.read_csv("https://raw.githubusercontent.com/ankita1112/House-Prices-Advanced-Regression/master/train.csv")

	obj = ColumnSelector('numerical')
	obj.fit(df)