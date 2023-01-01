import numpy as np
import pandas as pd
import bentoml as bml
from bentoml.io import NumpyNdarray, PandasDataFrame, JSON
from pydantic import BaseModel

# Runners
model_runner = bml.keras.get('bentomodel:latest').to_runner()
preproc_pipeline_runner = bml.sklearn.get('preproc_pipeline:latest').to_runner()


# Service
bentoservice = bml.Service('mort-pred', runners=[model_runner, preproc_pipeline_runner])

class PacientModel(BaseModel):
    SEXO: int = 1
    EDAD: int = 16
    EMBARAZO: int = 0
    DIABETES: int = 0
    EPOC: int = 0
    ASMA: int = 0
    INMUSUPR: int = 0
    HIPERTENSION: int = 0
    CARDIOVASCULAR: int = 0
    OBESIDAD: int = 0
    RENAL_CRONICA: int = 0
    TABAQUISMO: int = 0
    OTRA_COM: int = 0
    DIAS_SINTOMAS: int = 4

# Endpoints
@bentoservice.api(input=JSON(pydantic_model=PacientModel), output=NumpyNdarray())
def predict(data: PacientModel) -> np.array:
    df = pd.DataFrame(data.dict(), index=[0])
    # print(dir(preproc_pipeline_runner))
    # print(dir(model_runner))
    # Preprocess data
    preproc_data = preproc_pipeline_runner.transform.run(df)
    result = model_runner.predict.run(preproc_data) # TODO: Add args from orig function (e.g. verbose=0)
    return result