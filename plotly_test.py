import plotly.graph_objects as go
import numpy as np
import figures
import parse_api_output

np.random.seed(1)

timeline_dict = parse_api_output.parse_timeline()
fig = figures.fig_timeline(timeline_dict)

fig.show()