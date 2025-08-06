from pydantic import BaseModel

class PowRequest(BaseModel):
    base: int
    exponent: int

class FibRequest(BaseModel):
    n: int

class FactRequest(BaseModel):
    n: int

class ResultResponse(BaseModel):
    result: int
