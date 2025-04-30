import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

st.title("Smart Water Tank Simulation using Euler’s Method")

# User Inputs
inflow = st.slider("Inflow rate (L/min)", 0, 20, 10)
k = st.slider("Leakage constant (per min)", 0.0, 1.0, 0.1)
h0 = st.slider("Initial water level (liters)", 0, 100, 50)
time_minutes = st.slider("Simulation time (minutes)", 10, 120, 60)
max_capacity = 100  

# Euler’s Method
times = [0]
levels = [h0]
h = h0
for t in range(1, time_minutes + 1):
    dh_dt = inflow - k * h
    h += dh_dt
    h = min(max(h, 0), max_capacity)  
    levels.append(h)
    times.append(t)

def draw_tank(level):
    width, height = 150, 300
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

  
    draw.rectangle([20, 20, 130, 280], outline="black", width=3)

   
    fill_height = int((level / max_capacity) * 260) 
    top_y = 280 - fill_height
    draw.rectangle([21, top_y, 129, 279], fill="skyblue")

    return img

col1, col2 = st.columns(2)

with col1:
    st.subheader("Water Tank View")
    tank_img = draw_tank(levels[-1])
    st.image(tank_img)

with col2:
    st.subheader("Water Level Over Time")
    fig, ax = plt.subplots()
    ax.plot(times, levels, color='blue')
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Water Level (liters)")
    ax.set_title("Tank Level Simulation")
    ax.grid(True)
    st.pyplot(fig)