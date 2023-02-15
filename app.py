""" This version creates all the charts in the main app file rather than in create_charts.py"""
from pathlib import Path
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go


#-------
# Charts
#-------
#All of the path of files
BRENT_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'data','brent-daily.csv')
GAS_DAILY_FILEPATH = Path(__file__).parent.joinpath('data','gas-daily.csv')
BRENT_MONTH_FILEPATH = Path(__file__).parent.joinpath('data','brent-month.csv')
GAS_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'data','gas-monthly.csv')
WTI_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'data','wti-daily.csv')
WTI_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'data','wti-month.csv')
MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'monthly_file.csv')
DAILY_FILEPATH = Path(__file__).parent.joinpath( 'daily_file.csv')

# read from csv chart
cols = ['type','Date', 'Price']
df_brent_daily = pd.read_csv(BRENT_DAILY_FILEPATH, usecols=cols)
df_wti_daily = pd.read_csv(WTI_DAILY_FILEPATH, usecols=cols)
df_gas_daily = pd.read_csv(GAS_DAILY_FILEPATH, usecols=cols)
df_gas_monthly = pd.read_csv(GAS_MONTHLY_FILEPATH, usecols=cols)
df_wti_monthly = pd.read_csv(WTI_MONTHLY_FILEPATH, usecols=cols)
df_brent_monthly = pd.read_csv(BRENT_MONTH_FILEPATH, usecols=cols)
df_monthly= pd.read_csv(MONTHLY_FILEPATH, usecols=cols)
df_daily= pd.read_csv(DAILY_FILEPATH, usecols=cols)

#plot the first line graph
#daily brent graph
line_brent_daily = px.line(df_brent_daily, x='Date', y='Price', title='Brent Daily Price')
#daily wti graph
line_wti_daily = px.line(df_wti_daily, x='Date', y='Price',title='WTI Daily Price')
#daily gas graph
line_gas_daily = px.line(df_gas_daily, x='Date', y='Price',title='Gas Daily Price')
#put a title
line_brent_daily.update_layout(title="Prices Over Time")

#plot all the lines together
fig_1 = px.line()
fig_1.add_scatter(x=df_brent_daily['Date'], y=df_brent_daily['Price'], name='Brent Price')
fig_1.add_scatter(x=df_wti_daily['Date'], y=df_wti_daily['Price'], name='WTI Price')
fig_1.add_scatter(x=df_gas_daily['Date'], y=df_gas_daily['Price'], name='Gas Price')

#plot second bar chart
fig_2 = go.Figure()
fig_2.add_trace(go.Bar(x=df_brent_monthly['Date'], y=df_brent_monthly['Price'], name='Brent Price'))
fig_2.add_trace(go.Bar(x=df_wti_monthly['Date'], y=df_wti_monthly['Price'], name='WTI Price'))
fig_2.add_trace(go.Bar(x=df_gas_monthly['Date'], y=df_gas_monthly['Price'], name='Gas Price'))
fig_2.update_layout(title='Bar Chart')

#normal setting of dash app
app = Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            #"name": "viewport",
            "content": "width=device-width, initial-scale=1"
        },
    ],
)

#layout part
app.layout = dbc.Container(
[
    html.H1("Dashboard of Oil and Gas Prices"),
    html.Br(),
    html.H2("This chart shows the changes in Brent & WTI oil prices."),
    #cahrt 1
    dcc.Graph(id='line-daily', figure=fig_1),
    html.H2("This is a bar chart shows price of each month during the past 30 years."),
    #chart 2
    dcc.Graph(id='bar-daily', figure=fig_2),
    #space
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div
    ([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
        html.H1(children='Pattern Matching Graphs'),
        html.Br(),
        html.H2('In this chart, you can compare two price changes in a specific time period with two choosen graphs:'),
        dcc.Dropdown
            (
            id='category-dropdown',
            #3 options for chart to choose
            options=[
                    {'label': 'Gas', 'value': 'gas'},
                    {'label': 'WTI', 'value': 'wti'},
                    {'label': 'Brent', 'value': 'brent'}
                    ],
            value='gas'
            ),
            
        
        dcc.RadioItems(id='time-radio',value='daily'),
dcc.Graph(id='pattern-matching-graph'),

dcc.Dropdown
            (
            id='category-dropdown_2',
            options=[
                    {'label': 'Gas', 'value': 'gas'},
                    {'label': 'WTI', 'value': 'wti'},
                    {'label': 'Brent', 'value': 'brent'}
                    ],
            value='gas'
            ),

        dcc.RadioItems(id='time-radio_2',value='daily_2'),
dcc.Graph(id='pattern-matching-graph_2'),
         html.Div(dcc.Link('Return to first chart', href='/page-2')),
    ],
    
className="container-fluid"
),

],
fluid=True,
)

#callbakc part
@app.callback(
        #two graphs needs two outputs
    [Output('pattern-matching-graph', 'figure'), Output('pattern-matching-graph_2', 'figure')],
    [Input('category-dropdown', 'value'), Input('time-radio', 'value'), Input('category-dropdown_2', 'value'), Input('time-radio_2', 'value')]
)

#For the two graphs grab datas together
def update_graph(category, time, category_2, time_2):
    if category == 'gas':
        df = df_gas_daily
    elif category == 'wti':
        df = df_wti_daily
    elif category == 'brent':
        df = df_brent_daily
    else:
        raise ValueError(f'Invalid category: {category}')
    if time == 'daily':
        fig = px.line(df, x='Date', y='Price', title='Daily Prices')
    else:
        fig = px.line(df, x='Date', y='Price', title='Monthly Prices')
    if category_2 == 'gas':
        df_2 = df_gas_daily
    elif category_2 == 'wti':
        df_2 = df_wti_daily
    elif category_2 == 'brent':
        df_2 = df_brent_daily
    else:
        raise ValueError(f'Invalid category: {category_2}')
    if time_2 == 'daily_2':
        fig_2 = px.line(df_2, x='Date', y='Price', title='Daily Prices')
    else:
        fig_2 = px.line(df_2, x='Date', y='Price', title='Monthly Prices')
    return fig, fig_2


if __name__ == '__main__':
    app.run_server(debug=True)
