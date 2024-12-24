# Redbus
This project involves scraping bus data from RedBus using Selenium, storing it in an SQL database, and creating a Streamlit app for interactive user queries

# RedBus Data Scraping, SQL Integration, and Streamlit App

This project involves scraping bus data from the RedBus website using Selenium, storing it in an SQL database, and creating an interactive Streamlit app for users to explore and filter the data.

---

## Features

1. **Data Scraping**: 
   - Collect detailed bus information such as routes, prices, departure times, seat availability, and more.
   - Save the scraped data into CSV files.

2. **SQL Integration**: 
   - Store the data in a structured SQL database.
   - Use SQL queries to retrieve and manage the data efficiently.

3. **Streamlit App**:
   - Create an interactive web app to display the data.
   - Enable users to filter bus details based on routes, prices, seats, and other parameters.

---

## Tools and Technologies

- **Python**: For scripting and backend logic.
- **Selenium**: For automating data extraction from the RedBus website.
- **SQL**: For structured data storage and retrieval.
- **Streamlit**: For building an interactive web application.

---

## How to Use

### Step 1: Data Scraping with Selenium

1. Install Selenium:
   ```bash
   pip install selenium
   ```
2. Download the appropriate WebDriver for your browser (e.g., ChromeDriver).
3. Run the Python script to scrape data from RedBus:
   ```python
   import pandas as pd

   # Save scraped data to CSV
   data = pd.DataFrame(scraped_data)  # scraped_data is a list of dictionaries.
   data.to_csv('bus_data.csv', index=False)
   ```

### Step 2: Storing Data in SQL

1. Install MySQL Connector:
   ```bash
   pip install mysql-connector-python
   ```
2. Create a table in the SQL database:
   ```sql
   CREATE TABLE bus_details (
       id INT AUTO_INCREMENT PRIMARY KEY,
       route_name TEXT,
       route_link TEXT,
       busname TEXT,
       bustype TEXT,
       departing_time TIME,
       duration TEXT,
       reaching_time TIME,
       star_rating FLOAT,
       price DECIMAL(10, 2),
       seats_available INT
   );
   ```
3. Insert data from the CSV file:
   ```python
   import mysql.connector

   connection = mysql.connector.connect(
       host='your_host',
       user='your_user',
       password='your_password',
       database='your_database'
   )

   cursor = connection.cursor()

   with open('bus_data.csv', 'r') as file:
       next(file)  # Skip the header
       for row in file:
           cursor.execute(
               "INSERT INTO bus_details (route_name, route_link, busname, bustype, departing_time, duration, reaching_time,                     star_rating, price, seats_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               tuple(row.strip().split(','))
           )

   connection.commit()
   cursor.close()
   connection.close()
   ```

### Step 3: Building the Streamlit App

1. Install Streamlit:
   ```bash
   pip install streamlit
   ```
2. Create the app (`app.py`) with two pages:
   - **Introduction Page**: Explains the project.
   - **Bus Details Page**: Displays and filters bus details.
3. Sample code for the app:

   ```python
   import streamlit as st
   import pandas as pd
   import mysql.connector

   st.sidebar.title("Navigation")
   page = st.sidebar.radio("Go to", ["Introduction", "Bus Details"])

   if page == "Introduction":
       st.title("RedBus Data Project")
       st.write("This project collects bus data from RedBus and displays it interactively.")

   elif page == "Bus Details":
       connection = mysql.connector.connect(
           host='your_host',
           user='your_user',
           password='your_password',
           database='your_database'
       )

       query = "SELECT * FROM bus_details"
       data = pd.read_sql(query, connection)

       connection.close()

       route = st.sidebar.selectbox("Select Route", data['route_name'].unique())
       filtered_data = data[data['route_name'] == route]

       st.dataframe(filtered_data)
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## Future Improvements

- Add data visualization charts.
- Implement user authentication for personalized access.
- Enhance the app with real-time data updates.

---

## Acknowledgments

- Selenium for web scraping.
- MySQL for database management.
- Streamlit for creating the interactive web app.

contact : kishorekumarbn18@gamil.com
