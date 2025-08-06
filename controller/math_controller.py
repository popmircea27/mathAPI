# controller/math_controller.py

from fastapi import APIRouter, HTTPException
from database.db_operations import RequestDAO
from service import math_functions as math_service
from model.request_models import ResultResponse, PowRequest, FibRequest, FactRequest

router = APIRouter()

@router.post("/pow", response_model=ResultResponse)
def calc_pow(req: PowRequest):
    try:
        result = math_service.power(req.base, req.exponent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    dao = RequestDAO()
    dao.save_request("pow", req.model_dump_json(), str(result))
    dao.close()
    return {"result": result}

@router.post("/fibonacci", response_model=ResultResponse)
def calc_fib(req: FibRequest):
    try:
        result = math_service.fibonacci(req.n)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    dao = RequestDAO()
    dao.save_request("fibonacci", req.model_dump_json(), str(result))
    dao.close()
    return {"result": result}

@router.post("/factorial", response_model=ResultResponse)
def calc_fact(req: FactRequest):
    try:
        result = math_service.factorial(req.n)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    dao = RequestDAO()
    dao.save_request("factorial", req.model_dump_json(), str(result))
    dao.close()
    return {"result": result}
