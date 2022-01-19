"""
Author: Siddhant Mahajani
plotData.py - This is helpful to plot the data using matplotlib
"""

import plotly.graph_objects as go
from dataprep.eda import plot


def getdatainsights(data):
    fig = plot(data)
    fig.show_browser()


def plotdata(data):
    PLOT = go.Figure()
    for C in list(data.Cluster.unique()):
        PLOT.add_trace(go.Scatter3d(x=data[data.Cluster == C]['Income'],
                                    y=data[data.Cluster == C]['Seniority'],
                                    z=data[data.Cluster == C]['Spending'],
                                    mode='markers', marker_size=6, marker_line_width=1,
                                    name=str(C)))

    PLOT.update_traces(hovertemplate='Income: %{x} <br>Seniority: %{y} <br>Spending: %{z}')
    PLOT.update_layout(width=800, height=800, autosize=True, showlegend=True,
                       scene=dict(xaxis=dict(title='Income', titlefont_color='black'),
                                  yaxis=dict(title='Seniority', titlefont_color='black'),
                                  zaxis=dict(title='Spending', titlefont_color='black')),
                       font=dict(family="Gilroy", color='black', size=12))