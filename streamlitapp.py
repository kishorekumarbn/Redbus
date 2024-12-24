import pandas as pd
import numpy as np
import streamlit as st


p=st.sidebar.radio("PAGES :",["HOME","ENQUIRY"])
if p=="HOME":
    st.markdown("---")
    st.image("redbus_1200x768.jpg",width=1000)
    st.markdown("---")
    st.title("Welcome to REDBUS Data Enquiry")
    st.write("by KISHORE KUMAR B N")
    st.markdown("*This streamlit page has been created to access details fetched from redbus website.Naviagate to the next page ,Click the required routes and get the necessary details.*")
    st.write("😊 🚌")

if p=="ENQUIRY":
    st.markdown("---")
    st.image("India-BusTrack-Report123-1536x864.png",width=1000)
    st.markdown("---")
    st.title("Bus Routes Details Finder")
    st.markdown("---")
    #l=['ASTC.csv','BSRTC.csv','CTU.csv','JKSRTC.csv','KAAC.csv','KLTC.csv','NBSTC.csv','PEPSU.csv','WBSRTC.csv','WBTC.csv']
    csv_files = {
    "ASTC": "ASTC.csv",
    "BSRTC": "BSRTC.csv",
    "CTU": "CTU.csv",
    "JKSRTC": "JKSRTC.csv",
    "KAAC": "KAAC.csv",
    "KLTC": "KLTC.csv",
    "NBSTC": "NBSTC.csv",
    "PEPSU": "PEPSU.csv",
    "WBSRTC": "WBSRTC.csv",
    "WBTC": "WBTC.csv"
    }

    st.sidebar.header("Select Your Route")
    selected_route = st.sidebar.selectbox("Choose a State Transport", list(csv_files),index=None)

    data = pd.read_csv(csv_files[selected_route])
    data['Seat_Availability'] = data['Seat_Availability'].str.replace('Seats available', '', case=False, regex=True).str.replace('No seats available', '0', case=False, regex=True)
    data['Seat_Availability'] = data['Seat_Availability'].fillna('0').str.strip()
    data['Seat_Availability'] = pd.to_numeric(data['Seat_Availability'], errors='coerce')
    #st.write(data)

    st.subheader("Use necessary filters")

    #price
    min_price = int(data['Price'].min())
    max_price = int(data['Price'].max())
    price_range = st.sidebar.slider("Filter by Price Range", min_price, max_price, (min_price, max_price))

    #seat Availability
    min_seats = 0
    max_seats = int(data['Seat_Availability'].max())
    seats_available = st.sidebar.slider( "Filter by Seats Available",min_seats,max_seats,(min_seats, max_seats))

    #Bus type
    bus_types = data['Bus_Type'].unique()
    selected_bus_type = st.sidebar.multiselect("Filter by Bus Type", bus_types, default=bus_types)

    filtered_data = data[
    (data['Bus_Type'].isin(selected_bus_type)) &
    (data['Price'] >= price_range[0]) &
    (data['Price'] <= price_range[1]) &
    (data['Seat_Availability'] >= seats_available[0]) &
    (data['Seat_Availability'] <= seats_available[1])
    ]

    # Display Filtered Data
    st.write(filtered_data)