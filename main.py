# this models import is here in the directory
import models

# this database import is here in the directory
from database import SessionLocal, engine

import yfinance
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
# pydantic helps specify the structure of the requests
from pydantic import BaseModel
from models import Stock
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# global variable to store the template location
templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# this is the route for the home page (decorator)
@app.get("/")
def home(
    request: Request,
    forward_pe=None,
    dividend_yield=None,
    ma50=None,
    ma200=None,
    db: Session = Depends(get_db),
):
    """
    http://127.0.0.1:8000/
    Shows all stocks in the database and button to add more
    filters to filter this list of stocks
    TODO: button next to each stock to delete from database
    TODO: button next to each to add a note or save for later
    """

    # prefilter the stocks so that all stocks have price more than 0
    stocks = db.query(Stock).filter(Stock.price > 0)

    

    if forward_pe:
        stocks = stocks.filter(Stock.forward_pe < forward_pe)

    if dividend_yield:
        stocks = stocks.filter(Stock.dividend_yield > dividend_yield)

    if ma50:
        stocks = stocks.filter(Stock.price > Stock.ma50)

    if ma200:
        stocks = stocks.filter(Stock.price > Stock.ma200)

    stocks = stocks.all()

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "stocks": stocks,
            "dividend_yield": dividend_yield,
            "forward_pe": forward_pe,
            "ma200": ma200,
            "ma50": ma50,
        },
    )


def fetch_stock_data(id: int):

    db = SessionLocal()

    stock = db.query(Stock).filter(Stock.id == id).first()

    yahoo_data = yfinance.Ticker(stock.symbol)

    stock.ma200 = yahoo_data.info["twoHundredDayAverage"]
    stock.ma50 = yahoo_data.info["fiftyDayAverage"]
    stock.price = yahoo_data.info["previousClose"]
    stock.forward_pe = yahoo_data.info["forwardPE"]
    stock.forward_eps = yahoo_data.info["forwardEps"]
    stock.dividend_yield = yahoo_data.info["dividendYield"] * 100

    db.add(stock)
    db.commit()


# http://127.0.0.1:8000/docs#/default/create_stock_stock_post
@app.post("/stock")
# background tasks using async
async def create_stock(
    stock_request: StockRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    (Add empty lines in the comments to maintain
    formatting.)

    add one or more tickers to the database.

    e.g.
    SAM

    MSFT

    LAC

    IBM

    SLB

    SMPL

    background task to use yfinance and load key statistics
    """
    #instatiate the instance of Stock
    stock = Stock()
    stock.symbol = stock_request.symbol
    db.add(stock)
    db.commit()

    background_tasks.add_task(fetch_stock_data, stock.id)

    return {"code": "success", "message": "stock was added to the database"}
