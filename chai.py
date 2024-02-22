import streamlit as st
import requests
import time

# Function to fetch data from ThingSpeak
def fetch_data():
    url = "https://api.thingspeak.com/channels/YOUR_CHANNEL_ID/feeds.json?results=1"
    response = requests.get(url)
    data = response.json()
    return data['feeds'][0]

# Streamlit app
def main():
    st.title("Posture Management App")

    st.write("Accelerometer Data:")
    accelerometer_data = fetch_data()
    st.write("X-axis:", accelerometer_data['field1'])
    st.write("Y-axis:", accelerometer_data['field2'])
    st.write("Z-axis:", accelerometer_data['field3'])

    st.write("Gyroscope Data:")
    gyroscope_data = fetch_data()
    st.write("X-axis:", gyroscope_data['field4'])
    st.write("Y-axis:", gyroscope_data['field5'])
    st.write("Z-axis:", gyroscope_data['field6'])

    st.write("Flex Sensor Data:")
    flex_data = fetch_data()
    st.write("Flex Value:", flex_data['field7'])

    st.write("Last Updated:", flex_data['created_at'])

if __name__ == "__main__":
    main()
