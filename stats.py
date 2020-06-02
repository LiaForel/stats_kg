import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import seaborn as sns
from IPython.display import IFrame, HTML


from bubbly.bubbly import bubbleplot

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as py
import plotly.graph_objs as go
init_notebook_mode(connected=True) #do not miss this line
from plotly import tools



ftt = pd.read_csv('data/foreign_trade_turnover.csv', index_col = 0)
print(ftt)

x = ftt[ftt.Osh == 'Osh oblast']



