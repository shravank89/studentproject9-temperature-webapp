import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM world_temperature")
data = cursor.fetchall()
data_lists = list(map(list, zip(*data)))

st.title("World temperature data")


graph = px.line(x=data_lists[0], y=data_lists[1], labels={"y": "Temperature",
                                                          "x": "Date"})
st.plotly_chart(graph)