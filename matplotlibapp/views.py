import urllib.parse
from django.shortcuts import render,HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import urllib,base64


# data = pd.read_excel('matplotlibapp/media/new dataset.xlsx', engine='openpyxl')

# Create your views here.
def home(request):
    data = pd.read_csv('matplotlibapp\media\smartphones_cleaned_v6.csv')
    data["model"].value_counts().plot(kind='bar')
    plt.title("model")
    plt.xlabel('Category')
    plt.ylabel('Count')

    fig, ax = plt.subplots(figsize=(2, 2))


    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    uri = f"data:image/png;base64,{string}"
    buf.close()

    return render(request, 'matplotlibapp/graph.html', {'data': uri})