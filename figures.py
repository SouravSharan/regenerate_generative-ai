import plotly.graph_objects as go
import plotly.offline as py 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def fig_scatter():
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    return fig

def fig_network_graph():
    trace = go.Scatter( 
    x=[1, 2, 2, 1], 
    y=[3, 4, 3, 4], 
    mode='markers',
    marker=dict(size=[100, 100, 100, 100])
    )

    # Edges
    x0 = [1, 2]
    y0 = [3, 3]
    x1 = [2, 1]
    y1 = [4, 4]

    fig = go.Figure(
        data=[trace],
        layout=go.Layout(
            annotations = [
                dict(ax=x0[i], ay=y0[i], axref='x', ayref='y',
                    x=x1[i], y=y1[i], xref='x', yref='y',
                    showarrow=True, arrowhead=1,) for i in range(0, len(x0))
            ]
        )
    )

    return fig


def fig_timeline(timeline_dict):
    #fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])

    x_len = len(timeline_dict['events'])

    y_axis = [1 for e in range(x_len+5)]
    fig = go.Figure([go.Scatter(x=timeline_dict['dates'], y=y_axis, text=timeline_dict['events'], textposition="bottom center" , mode='lines+markers')])

    

    ay_lst = [30,120,90,60,180,150]
    flag = 0

    for itr in range(x_len):
        if itr%2 == 0:
            fig.add_annotation(
                xref="x domain",
                yref="y domain",
                # The arrow head will be 25% along the x axis, starting from the left
                x=(itr+1)/x_len,
                # The arrow head will be 40% along the y axis, starting from the bottom
                y=0.5,
                ay=ay_lst[flag],
                #yshift=-100,
                text=timeline_dict['events'][itr],
                arrowhead=2,
                #textangle=-90
            )
        else:
            
            fig.add_annotation(
                xref="x domain",
                yref="y domain",
                # The arrow head will be 25% along the x axis, starting from the left
                x=(itr+1)/x_len,
                # The arrow head will be 40% along the y axis, starting from the bottom
                y=0.5,
                ay=-ay_lst[flag],
                #yshift=100,
                text=timeline_dict['events'][itr],
                arrowhead=2,
                #textangle=-90
            )
            if flag == 5:
                flag = 0
            else:
                flag+=1

    return fig

