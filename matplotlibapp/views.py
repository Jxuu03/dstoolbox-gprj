import matplotlib
matplotlib.use('Agg')

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
      
    # โหลดข้อมูล
    data = pd.read_csv('matplotlibapp/media/smartphones_cleaned_v6.csv')

    # สร้างกราฟ
    fig, ax = plt.subplots(figsize=(6, 4))  # กำหนดขนาดกราฟ
    data["brand_name"].value_counts().plot(kind='bar', ax=ax)  # ใช้ ax ที่กำหนด
    ax.set_title("brand_name Distribution")
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # แปลงกราฟเป็น Base64
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    uri = f"data:image/png;base64,{string}"
    buf.close()

    return render(request, 'matplotlibapp/graph.html', {'data': uri})