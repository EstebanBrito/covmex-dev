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

# Input validation models
# Default values in Pacient Model are shown as examples in the 
# web API documentation, but automatically fill inputs that were not
# defined in client's request.
# TODO: Add automatic documentation of examples, whilst enforcing
# a policy that asks the client for every field on information
class PacientModel(BaseModel):
    SEXO: int
    EDAD: int
    EMBARAZO: int
    DIABETES: int
    EPOC: int
    ASMA: int
    INMUSUPR: int
    HIPERTENSION: int
    CARDIOVASCULAR: int
    OBESIDAD: int
    RENAL_CRONICA: int
    TABAQUISMO: int
    OTRA_COM: int
    DIAS_SINTOMAS: int

# Endpoints
@bentoservice.api(input=JSON(pydantic_model=PacientModel), output=NumpyNdarray(shape=[1, 1], dtype=np.float64))
def predict(data: PacientModel) -> np.array:
    # Preprocess input data
    df = pd.DataFrame(data.dict(), index=[0])
    preproc_data = preproc_pipeline_runner.transform.run(df)
    # Make predictions
    predictions = model_runner.predict.run(preproc_data) # TODO: Add args from orig function (e.g. verbose=0)
    # Preprocess predictions
    predictions = predictions # TODO: Convert to json
    return predictions