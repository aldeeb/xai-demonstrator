from typing import Any, Dict, Union

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, StrictFloat, StrictInt, ValidationError, validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .config import settings
from .explainer.explain import EXPLAINERS, Explanation, explain
from .model.predict import Prediction, predict

api = APIRouter()


@api.post("/predict")
def predict_weather(file: UploadFile = File(...)) -> Prediction:
    return predict(file.file)


class ExplanationRequest(BaseModel):
    method: str = settings.default_explainer
    settings: Dict[str, Union[StrictInt, StrictFloat, int, float, str]]

    @validator("method")
    def method_must_be_available(cls, v):
        if v not in EXPLAINERS:
            raise ValueError(f"{v} is not an available explanation method")
        return v


@api.post("/explain")
def explain_classification(file: UploadFile = File(...),
                           method: str = Form(settings.default_explainer),
                           exp_settings: Dict[str, Any] = Form({})) -> Explanation:
    try:
        request = ExplanationRequest(method=method,
                                     settings=exp_settings)
    except ValidationError as errors_out:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail=errors_out.errors()
        )

    return explain(file.file, method=request.method, settings=request.settings)
