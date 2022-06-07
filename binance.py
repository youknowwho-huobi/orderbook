import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

r = requests.get("https://api.binance.com/api/v3/depth",
                 params=dict(symbol="ETHBUSD"))
results = r.json()
