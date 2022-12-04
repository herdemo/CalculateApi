import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Calculate(BaseModel):
    FirstNumber: float
    SecondNumber: float


class CalculateResponse(BaseModel):
    Addition: float
    Subtraction: float
    Multiplication: float
    Division: float

    class Config:
        orm_mode = True


def Operation(firstNumer, secondNumber):
    CalculateResponse.Addition = firstNumer + secondNumber
    CalculateResponse.Subtraction = firstNumer - secondNumber
    CalculateResponse.Multiplication = firstNumer * secondNumber
    CalculateResponse.Division = firstNumer / secondNumber
    return CalculateResponse


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/calculate", response_model=CalculateResponse)
async def calculate_Number(cal: Calculate):
    return Operation(cal.FirstNumber, cal.SecondNumber)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)