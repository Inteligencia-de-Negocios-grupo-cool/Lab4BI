from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
from joblib import load
import numpy as np
from sklearn.metrics import mean_squared_error as mse
app = FastAPI()
class DataModelapp(BaseModel):
    Adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    Schooling: float
class DataPrediccion(BaseModel):
    Life_expectancy: float
    Adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    Schooling: float
class ListPrediccion(BaseModel):
    datos:List[DataModelapp]=None
class ListError(BaseModel):
    datos:List[DataPrediccion]=None
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]
@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/Data/predict")
async def make_prediction(dataModel: DataModelapp):
    
    df = pd.DataFrame(dataModel.dict(),index=[0])
    df.rename(columns={'Adult_mortality':'Adult Mortality','income_composition_of_resources':'Income composition of resources'},inplace=True)
    
    #df.columns = dataModel.columns()
    model = load("../pipelinelab4.joblib")
    result = model.predict(df)
    resultado=result[0]
    return {"Tiempo de expectativa de vida: ": resultado}
  

@app.post("/Data/predict/list")
async def make_predictionsList(dataList: ListPrediccion):
    lista_datos=dataList.dict()['datos']
    model = load("../pipelinelab4.joblib")
    respuestastr=''
    for i in lista_datos:
        df = pd.DataFrame(i,index=[0])
        df.rename(columns={'Adult_mortality':'Adult Mortality','income_composition_of_resources':'Income composition of resources'},inplace=True)
        result = model.predict(df)
        resultado=result[0]
        respuestastr=respuestastr+' , '+str(resultado)
    
    return {"Tiempos de expectativa de vida de cada set de datos: ": respuestastr}
@app.post("/Data/predict/Rcuadrado/list")
async def RMSE(dataList: ListError):
    lista_datos=dataList.dict()['datos']
    model = load("../pipelinelab4.joblib")
    resultado=[]
    valorEsperadoY={}
    dataframe=pd.DataFrame()
    dataframe_y=pd.DataFrame()
    for i in lista_datos:
        valorEsperadoY['Life_expectancy']=i['Life_expectancy']
        del i['Life_expectancy']
        df_y = pd.DataFrame(valorEsperadoY,index=[0])
        df_y.rename(columns={'Life_expectancy':'Life expectancy'},inplace=True)
        df = pd.DataFrame(i,index=[0])
        df.rename(columns={'Adult_mortality':'Adult Mortality','income_composition_of_resources':'Income composition of resources'},inplace=True)
        dataframe=pd.concat([dataframe,df])
        dataframe_y=pd.concat([dataframe_y,df_y])
    rcuadrado=model.score(dataframe,dataframe_y)
    
    return {"Error r ^2: ": rcuadrado} 