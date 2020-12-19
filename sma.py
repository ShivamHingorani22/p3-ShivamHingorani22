import argparse
import pprint
import yfinance as yf
import plotly.graph_objects as go


def chart(df, symbol, sma_name):
    candlestick = go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        name=symbol)
    sma = go.Scatter(x=df.index, y=df['sma'],
                     name=sma_name, line={'color': 'blue'})

    fig = go.Figure(data=[candlestick, sma])
    fig.layout.xaxis.type = 'category'
    fig.layout.xaxis.rangeslider.visible = False
    fig.show()


parser = argparse.ArgumentParser(
    description='Provide arguments for plotting Simple Moving Average')

parser.add_argument(
    '--symbol', '-s', help='stock ticker', required=True)
parser.add_argument('--period', '-p',
                    type=str,
                    choices=['1d', '5d', '1mo', '3mo', '6mo',
                             '1y', '2y', '5y', '10y', 'ytd', 'max'],
                    help='data period to analyze stock', default='1y')
parser.add_argument('--window', '-w',
                    help='number of periods in moving average', default=20)

args = vars(parser.parse_args())

pprint.pprint(args)

symbol = args['symbol']
period = args['period']
window = int(args['window'])

data = yf.download(symbol, period=period)
data['sma'] = data['Close'].rolling(window=window).mean()

sma_name = '{} period SMA'.format(window)
chart(data, symbol, sma_name=sma_name)
