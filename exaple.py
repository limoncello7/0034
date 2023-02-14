""" This version creates all the charts in the main app file rather than in create_charts.py"""
from pathlib import Path
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px


#-------
# Charts
#-------

BRENT_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'brent-daily.csv')
GAS_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'gas-daily.csv')
BRENT_MONTH_FILEPATH = Path(__file__).parent.joinpath('brent-month.csv')
GAS_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'gas-monthly.csv')
WTI_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'wti-daily.csv')
WTI_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'wti-month.csv')


cols = ['Date', 'Price']
df_brent_daily = pd.read_csv(BRENT_DAILY_FILEPATH, usecols=cols)
df_wti_daily = pd.read_csv(WTI_DAILY_FILEPATH, usecols=cols)
df_gas_daily = pd.read_csv(GAS_DAILY_FILEPATH, usecols=cols)
df_gas_monthly = pd.read_csv(GAS_MONTHLY_FILEPATH, usecols=cols)
df_wti_monthly = pd.read_csv(WTI_MONTHLY_FILEPATH, usecols=cols)
df_brent_monthly = pd.read_csv(BRENT_MONTH_FILEPATH, usecols=cols)









line_brent_daily = px.line(df_brent_daily, x='Date', y='Price', title='Brent Daily Price')

line_wti_daily = px.line(df_wti_daily, x='Date', y='Price',title='WTI Daily Price')

line_brent_daily.update_layout(title="Prices Over Time")
fig_1 = px.line()
fig_1.add_scatter(x=df_brent_daily['Date'], y=df_brent_daily['Price'], name='Brent Price')
fig_1.add_scatter(x=df_wti_daily['Date'], y=df_wti_daily['Price'], name='WTI Price')



app = Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            #"name": "viewport",
            "content": "width=device-width, initial-scale=1"
        },
    ],
)

app.layout = dbc.Container(
    [
        html.H1("Dashboard of oil and gas prices"),
        html.H2("This chart is showing how Brent&WTI oil price changes"),
        dcc.Graph(
            id='line-daily',
            figure=fig_1
        ),
        html.H2("This chart is showing the trend of brent price changes compare to the change of gas price"),

    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
