import streamlit as st
import plotly.express as px
from backend import get_data

# Add front end
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")


if place:

# get the data from the function

    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [i['main']['temp'] for i in filtered_data]
        dates = [j["dt_txt"] for j in filtered_data]
        # Create a temperature graph
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        images = {"Clouds": "images/cloud.png", "Snow": "images/snow.png",
                  "Rain": "images/rain.png", "Clear": "images/clear.png"}

        conditions = [k["weather"][0]["main"] for k in filtered_data]
        print(conditions)
        image_paths = [images[condition]for condition in conditions]
        st.image(image_paths, width=115)
