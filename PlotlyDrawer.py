import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import mySqlConnector as sql
import plotly

plotly.tools.set_credentials_file(username='DamianFaustryjak', api_key='tFCuvXghk8z6FYPAlBvP')

def draw(name,open,close,max,min,dates):
    py.get_credentials()
    open = sql.search(name,"open");
    close = sql.search(name,"close");
    max = sql.search(name,"max");
    min = sql.search(name,"min");
    dates = sql.search(name,"date");
    fig = FF.create_candlestick(open, max, min, close, dates)
    py.iplot(fig, filename=name, validate=False, )


