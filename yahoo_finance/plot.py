import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv("aapl.csv")
candlestick = go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

fig = go.Figure(data=[candlestick])
# fig.show()
fig.layout.xaxis.type = "category"

shapes = [dict(
        x0='2020-03-23', x1='2020-03-23', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)]

annotations=[dict(
        x='2020-03-23', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='covid-19 becomes worse')]

fig.update_layout(
    title='Coronavirus Boom',
    yaxis_title='AAPL Stock',
    shapes=shapes,
    annotations=annotations
)

fig.write_html("aapl.html", auto_open=True)


