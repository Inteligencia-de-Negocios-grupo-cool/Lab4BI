from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
from joblib import load
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

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]
@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/Data/predict")
async def make_predictions(dataModel: DataModelapp):
    
    df = pd.DataFrame(dataModel.dict(),index=[0])
    df.rename(columns={'Adult_mortality':'Adult Mortality','income_composition_of_resources':'Income composition of resources'},inplace=True)
    
    #df.columns = dataModel.columns()
    model = load("../pipelinelab4.joblib")
    result = model.predict(df)
    resultado=result[0]
    return {"Tiempo de expectavida de vida: ": resultado}
            
    