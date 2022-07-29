
# Global cases of monkeypox in the world from raw data


import plotly.graph_objs as go
import pandas as pd 


url = 'https://raw.githubusercontent.com/globaldothealth/monkeypox/main/timeseries-confirmed.csv'

df_world = pd.read_csv(url)
df_world['Rolling Ave_cum'] = df_world['Cumulative_cases'].rolling(window=30).mean().fillna(0)


####indicator###
fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = df_world['Cumulative_cases'].iloc[-1],
    delta = {"reference": df_world['Cumulative_cases'].iloc[-2], "valueformat": ".0f"},
    title = {"text": "Global Cases"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]},
    number = {'valueformat':','},
                 #delta_increasing_symbol = "↖︎",
                  delta_increasing_color = 'red',
                 align = 'center'
))

###add line chart ###
fig.add_trace(
    go.Scatter(
        name = "Cumulative Cases",
        mode = 'lines',
        x = df_world['Date'],
        y = df_world['Cumulative_cases'],
       
))

fig.add_trace(
    go.Scatter(
        name = "Monthly Rolling Av",
        mode = "lines",
        x = df_world['Date'], 
        y = df_world['Rolling Ave_cum']
    )
)

fig.update_layout(
    title = dict(text = "MonkeyPox World Cumulatives Cases<br><span style ='font-size: 0.7em;  color:gray'>Last Update : " + 
                               df_world['Date'].iloc[-1] + "</span>",
                y= 0.93), 
    template = "simple_white",
    hovermode ="x",
    width = 850,
    legend = {'orientation':'h',
              'x':0.7, 
              'y': 1,
              'xanchor':'center',
              'yanchor':'bottom'},                
     
     xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=2,
                     label="2 months",
                     step="month",
                     stepmode="backward"),
                dict(count=5,
                     label="3 months",
                     step="month",
                     stepmode="backward"),
                dict(step="all")])
        ),
        title = "Date" 
    ),
                  
     yaxis = dict(title = "NB of Cases")             
)


# add line and annotations #
fig.add_vline(x ="2022-05-06", line_width=1, 
              line_dash="dash", line_color="blue", opacity = 0.8)

fig.add_annotation( # add a text callout with arrow
    text="Non-endemic Countries first Cases ",
    font = dict(color = 'blue'),
    x="2022-05-06", y=1000, arrowhead=1, showarrow=True
)

fig.show()
