# Run this app with `Info_Viz_Project.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
app = Dash(__name__)

# see https://plotly.com/python/px-arguments/ for more options

# Creating the Panda's data frames that are used in the plotly figures
df_t1 = pd.read_excel('Task1.xlsx','Top_15')
df = pd.read_excel('Task2.xlsx','Well_Processed_Data')
df_t3_1 = pd.read_excel('Task3.xlsx','Correlation_Developed_Temp_Foss')
df_t3_2 = pd.read_excel('Task3.xlsx','Correlation_Develping_Temp_Foss')
df_t4 = pd.read_excel('Task4.xlsx','Seasons_Consolidated')
df_t4_1 = pd.read_excel('Task4.1.xlsx','Task4.1')

fig_task1 = px.histogram(df_t1,x='Country_Name',y='Average',color_discrete_sequence=['#44C993'])
fig_task2 = px.line(df,x='Year',y=['Developing','Developed','World'])
fig_task3_1 = px.scatter(df_t3_1, x="Developed (Temp_Change)", y="Developed (Fossil_Fuel)",color='Year', trendline="ols")
fig_task3_2 = px.scatter(df_t3_2, x="Developing (Temp_Change)", y="Developing (Fossil_Fuel)", color='Year', trendline="ols")
fig_task4 = px.line(df_t4,x='Year',y=['Winter','Spring','Summer','Fall'],color_discrete_sequence=['brown', 'blue','red','orange'])

fig_task4_1 = fig = px.sunburst(df_t4_1, labels='Temperature_Change',
                              path=['Economy','Season'], values='Temperature_Change',
                              color='Temperature_Change', width=900,height=600,
                              color_continuous_scale='RdBu',color_continuous_midpoint=np.average(df_t4_1['Temperature_Change'])                       
                              )


app.layout =html.Div(children=[
    html.H1('Information Visualization Project by Team N',style={ 'padding': '40px','font-color':'black', 'text-align': 'center','background':'#2AC3C8','color': 'white','font-size': '30px'}),
    html.H1(children='Task 1: Top 15 Countries affected by the temperature change.',),
    dcc.Graph(
        id = 'task1',
        figure = fig_task1       
    ),
    html.H1(children='Task 2: Analyzing the temperature change patterns of developed and developing countries.',),
    html.Div([
        html.P('From the figure it can be observed that the Temperatue change in the developed countries was higher than the developing countries.'),
        ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='task2', 
        figure=fig_task2
    ),
    html.H1(children='Task 3.1: Analyzing the consumption of fossil fuels in developed countries and its relation to Temperature change.',),
    html.Div([
        html.P('Negative Correlation is observed between the temperature change and fossil fuel consumption in developed countries.'),
        ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='task3_1',
        figure=fig_task3_1
    ),
    html.H1(children='Task 3.2: Analyzing the consumption of fossil fuels in developing countries and its relation to Temperature change.',),
     html.Div([
         html.P('Positive Correlation is observed between the temperature change and fossil fuel consumption in developing countries.'),
         ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='task3_2',
        figure=fig_task3_2
    ),
    html.H1(children='Task 4: Analyzing the effect of season on temperature change.',),
     html.Div([
         html.P("It's an interesting comparison, we can see that temperature change fluctuates during different years."),
         ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='task4',
        figure=fig_task4
    ),
    html.H1(children='Task 4.1: Analyzing the effect of season on temperature change.',),
     html.Div([
         html.P("It's an interesting comparison, in the below sunburst chart the color is used to show the values of Temperature change"),
         ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='task6',
        figure=fig_task4_1
    ),
    html.H1(children='Task 4: Analyzing the effect of season on temperature change [From Treemap-4.1.2].',),
     html.Div([
         html.P("Plotted Treemaps using Treemap-4.1.2 software by Universsity of Maryland, this is a screenshot for reference. Visual is best viewed in Treemap-4.1.2"),
         ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    html.Img(src=r'assets/Treemap.jpg',width = '900', height='600', alt='image'),
    html.H1(children='Task 5: Analyzing the effect of seasons on Temperature change in developed and developing countries.[From Treemap-4.1.2].',),
     html.Div([
         html.P("Plotted Treemaps using Treemap-4.1.2 software by Universsity of Maryland, this is a screenshot for reference. Visual is best viewed in Treemap-4.1.2"),
         ],style={  'color': 'brown', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    html.Img(src=r'assets/Treemap_5.jpg',width = '900', height='600', alt='image')
])

if __name__ == '__main__':
    app.run_server(debug=True)
