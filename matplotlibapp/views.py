import matplotlib

matplotlib.use('Agg')

import urllib.parse
from django.shortcuts import render, HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.io as pio
import io
import urllib, base64


# data = pd.read_excel('matplotlibapp/media/new dataset.xlsx', engine='openpyxl')

# Create your views here.
def home(request):
    data = pd.read_csv('matplotlibapp/media/smartphones_cleaned_v6.csv')

    fig, ax = plt.subplots(figsize=(6, 4))
    data["brand_name"].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("brand_name Distribution")
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    uri = f"data:image/png;base64,{string}"
    buf.close()

    return render(request, 'matplotlibapp/graph.html', {'data': uri})


def pie(request):
    df = pd.read_csv('matplotlibapp/media/smartphones_cleaned_v6.csv')

    data = df['internal_memory'].value_counts()
    labels = data.index
    sizes = data.values

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors
    )
    ax.set_title("Internal Memory Distribution by Brand")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    graph_data = base64.b64encode(buf.read()).decode()
    buf.close()

    return render(request, 'matplotlibapp/pie.html', {'graph': graph_data})


def top_5(request):
    data = pd.read_csv('matplotlibapp/media/smartphones_cleaned_v6.csv')

    top_5 = data["brand_name"].value_counts().head(5)

    fig, ax = plt.subplots(figsize=(6, 4))
    top_5.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title("Top 5 Models")
    ax.set_xlabel('Model')
    ax.set_ylabel('Count')

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    graph_data = base64.b64encode(buf.read()).decode()
    buf.close()

    return render(request, 'matplotlibapp/top_5.html', {'data': graph_data, 'top_5': top_5.to_dict()})
