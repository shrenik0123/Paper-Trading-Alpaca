import yfinance as yf
import numpy as np
import pandas as pd

aapl = yf.Ticker("AAPL")
hist = aapl.history(period="2y")
path = "./aapl.csv"
hist.to_csv(path)