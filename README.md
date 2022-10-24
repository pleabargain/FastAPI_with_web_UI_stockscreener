# URL for this repo
https://github.com/pleabargain/FastAPI_with_web_UI_stockscreener

I have been looking for a complete FastAPI | DB | Jinja template | web app. I am hoping this one will be it! So far so good. Take a look at the video series too: https://www.youtube.com/watch?v=HVZUJb1_Jm8

# pip install -r requirements
If I run that in the command line
```pip install -r requirements.txt``` and I have a requirements.txt file in my base directory, all of the python libs will be installed. I didn't know that! :)

----

# installed yfinance
```pip install yfinance```
I manually installed yfinance because I knew I had the other libs.


I have no idea what it does but I'm guessing it's Yahoo Finance connection.

---

# VS Code
start a terminal

```ctrl + ~```

Make sure ```main.py``` is there

```ls```
then run 
```uvicorn main:app --reload```

go to http://127.0.0.1:8000/

when I try to add a symbol, "GE" for example, I get an error.
```cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: stocks.symbol     
[SQL: INSERT INTO stocks (symbol, price, forward_pe, forward_eps, dividend_yield, ma50, ma200) VALUES (?, ?, ?, ?, ?, ?, ?)]
[parameters: ('GE', None, None, None, None, None, None)]
(Background on this error at: https://sqlalche.me/e/14/gkpj)
```

but then I click on Filter button and my two entries were loaded! Yay!

---

http://127.0.0.1:8000/

Shows all stocks in the db

---

http://127.0.0.1:8000/docs

Shows all the docs for the API


---

I added a basic sql query to this project. I could populate the whole db 

---

# sqlalchemy
object relational mapper (ORM) for querying databases

---

# TODO 
* read up on semantic ui and find out if there are other projects like that one
* Add a confirmation message for user stating that "X symbol has been added".
* If stock value = None then highlight the row
* way to remove unwanted stocks
* way to add notes to a particular stock
---

# original README
Didn't see a lot of examples out there for this framework, so decided to create one.

## Step 1: Hello World of FastAPI, Stub out the API endpoints

* Display Hello World
* Map out endpoints we will need, comment what they will do

## Step 2: Mock the UI with Semantic UI and Jinja2 Templates

* Including CSS and JavaScript from the CDN

## Step 3: Database Design

* To design our database, we create SQLAlchemy models
* See what yfinance provides 
* forwardPE, forwardEps, dividendYield, 50 Day, 200 Day, Close
* SQLAlchemy create_all

## Step 4: Add a stock endpoint

* Background task to fetch info and add to db also
* Use Insomnia to test it

## Step 5: Wire home screen

* Show added stocks in a table

## Step 6: Filters to filter table

* Filter boxes on UI
* Use SQLALchemy to filter in db
* Use query parameters to filter
 
## Step 7: Modal to add stock tickers via UI
