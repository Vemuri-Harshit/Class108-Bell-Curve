import math;
import numpy;
import random;
import plotly.express as px;
import plotly.figure_factory as ff;
import pandas as pd;
import csv;

df = pd.read_csv('proof_2.csv');

graph = ff.create_distplot([df['Index'].tolist()] ,['count'], show_hist = False);

graph.show();