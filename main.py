from typing import Optional

from fastapi import FastAPI 
from pydantic import BaseModel

from fund_calculator import *

app = FastAPI(
    title="CalcInvest API",
    description="This is the documentation for the CalcInvest API.",
    version="0.0.1",
) 

class Item(BaseModel):
    name: str
    price: float 
    is_offer: Optional[bool] = None

class fundSavingsFormClass(BaseModel):
    startingEquity: int #                  = IntegerField('startingEquity', validators=[NumberRange(min=0, max=999999999, message='Outside range')], render_kw={"placeholder": "Write a number..."})
    interestRatePercent: float #             = DecimalField('interestRatePercent', validators=[NumberRange(min=0, max=100, message='Outside range')], render_kw={"placeholder": "Write a number..."})
    numYears: int         #                = IntegerField('numYears', validators=[NumberRange(min=0, max=1000, message='Outside range')], render_kw={"placeholder": "Write a number..."})
    savingsPerMonth: int  #              = IntegerField('savingsPerMonth', validators=[NumberRange(min=0, max=999999999, message='Outside range')], render_kw={"placeholder": "Write a number..."})
    costOfFund: float     #                 = DecimalField('costOfFund', validators=[NumberRange(min=0, max=100, message='Outside range')], render_kw={"placeholder": "Write a number..."})
    taxRate: float        #                 = DecimalField('taxRate', validators=[NumberRange(min=0, max=100, message='Outside range')], render_kw={"placeholder": "Write a number..."})


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fund_calculator/")
def fund_calculator(fund_savings: fundSavingsFormClass):

    fundSavingsDict = dict()

    fundSavingsDict['startingEquity']       = int(fund_savings.dict()['startingEquity'])
    fundSavingsDict ['numYears']            = int(fund_savings.dict()['numYears'])
    fundSavingsDict ['numMonths']           = int(fund_savings.dict()['numYears']) * 12

    fundSavingsDict['interestRatePercent']  = float(fund_savings.dict()['interestRatePercent'])
    fundSavingsDict['interestRate']         = (fundSavingsDict['interestRatePercent']  / 100) + 1
    fundSavingsDict['interestRateMoM']      = round(fundSavingsDict['interestRate'] ** (1 / 12),4)

    fundSavingsDict['savingsPerMonth']      = int(fund_savings.dict()['savingsPerMonth'])
    fundSavingsDict['costOfFund']           = float(fund_savings.dict()['costOfFund']) / 100
    fundSavingsDict['costOfFund_percent']   = float(fund_savings.dict()['costOfFund'])

    fundSavingsDict['taxRate']              = float(fund_savings.dict()['taxRate']) / 100
    fundSavingsDict['taxRate_percent']      = float(fund_savings.dict()['taxRate'])

    fundSavingsDict, df_fundsavings = fundSavingsROI(fundSavingsDict)

    #starting_equity_times_two = starting_equity * 2

    return {**fundSavingsDict, **df_fundsavings.to_dict()}#"starting_equity": starting_equity_times_two, "interest":interest, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}