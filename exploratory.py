# Universidad del Valle de Guatemala
# Mineria de Datos
# HDT1-Exploratory Analysis
#------------------------------------
# Oliver de Leon 19270

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
from reader import reader as Reader

class main(object):

    def __init__(self, csvDoc, limitedYear):
        # Universal Doc
        self.csvDoc = csvDoc
        # Classes
        R = Reader(csvDoc)
        self.df = R.fuel
        self.limitedYear = limitedYear
        self.grooming()
        
        #self.df = self.rangeAdding(self.percentile())
        #self.remodel_bool()
    def grooming(self):
        self.df['Date'] = self.df.index
        self.df['Date_copy'] = self.df['Date'].dt.year

        if self.limitedYear:
            self.df = self.df[self.df['Date_copy'] >= self.limitedYear]

        #self.df = self.df[['Gasolina superior', 'Gasolina regular', 'Diesel']]
    
    
    def BestSaleMonth(self, fuel):
        df = self.df
        df['Date'] = df['Date'].dt.month
        df = df[['Gasolina superior','Gasolina regular', 'Diesel', 'Diesel bajo azufre', 'Date']]
        df = df.groupby('Date').mean()
        df = df.sort_values(fuel, ascending=False)
        title = ''
        
        if self.limitedYear:
            title = 'Meses con mayor importacion de ' + fuel 
        else:
            title = 'Meses con mayor consumo de ' + fuel 
        xLabel = 'Meses'
        yLabel = 'Barriles de ' + fuel
        ax = df.plot.bar(y=fuel, use_index=True)
        plt.title(title)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        #plt.locator_params(axis='x', nbins=12)
        plt.show()

    def bestYearSale(self, fuel):
        df = self.df
        df['Date'] = df['Date'].dt.year
        df = df[['Gasolina superior','Gasolina regular', 'Diesel', 'Date']]
        df = df.groupby('Date').mean()
        df = df.sort_values(fuel, ascending=False)
        
        title = ''
        if self.limitedYear:
            title = 'Importacion de ' + fuel + ' a lo largo de los años' 
        else:
            title = 'Consumo de ' + fuel + ' a lo largo de los años' 

        xLabel = 'Años'
        yLabel = 'Barriles de ' + fuel
        ax = df.plot.bar(y=fuel, use_index=True)
        plt.title(title)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        #plt.locator_params(axis='x', nbins=12)
        plt.show()
        

path = ['./data/CONSUMO-2022-05.xlsx','./data/IMPORTACION-VOLUMEN-2022-05.xlsx']
fuel = 'Gasolina superior'
limitedYear = 2018
exp = main(path[1], limitedYear)

exp.BestSaleMonth(fuel)
# exp.bestYearSale(fuel)