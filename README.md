# Redbus
This project involves scraping bus data from RedBus using Selenium, storing it in an SQL database, and creating a Streamlit app for interactive user queries
# RedBus Data Scraping, SQL Integration, and Streamlit App

Discover the magic of automation as we journey through extracting bus details from the RedBus website, organizing the data in an SQL database, and presenting it with an interactive Streamlit application. This beginner-friendly project combines Selenium, SQL, and Streamlit to create a seamless data pipeline.

---

## Project Highlights

1. **Data Scraping with Selenium**:
   - Unearth bus details like routes, seats available, prices, departure times, and more.
   - Traverse multiple pages of the RedBus website to ensure no detail is left behind.
   - Save the scraped data into CSV files for future use.

2. **Organized Data Storage with SQL**:
   - Create and configure a structured SQL database.
   - Load CSV data into SQL tables with clean formatting.
   - Enable easy retrieval of information for your applications.

3. **Interactive Streamlit App**:
   - Build a user-friendly interface to view and filter bus details.
   - Empower users to select routes, filter by price, and check seat availability.

---

## How It Works

### 1. Data Scraping with Selenium
- **Tools Used**: Selenium WebDriver.
- **Steps**:
  - Automate RedBus website navigation.
  - Extract bus details dynamically.
  - Save data into CSV files.

### 2. Data Storage in SQL Database
- **Tools Used**: MySQL (XAMPP or TiDB Cloud).
- **Steps**:
  - Create an SQL table for storing bus data.
  - Load data from CSV files into the database.
  - Use SQL queries for efficient data handling.

### 3. Streamlit App Development
- **Tools Used**: Streamlit Framework.
- **Steps**:
  - Design an intuitive interface for users.
  - Fetch data from the SQL database.
  - Enable filtering by route, price, and seat availability.

---

## Setting Up the Project

### Prerequisites
- **Python Libraries**:
  ```bash
  pip install selenium mysql-connector-python pandas streamlit
  ```
- **WebDriver**: Download the WebDriver compatible with your browser.
- **SQL Database**: Set up MySQL locally or use a cloud database.

### Running the Project
1. **Selenium Scraping**:
   - Run the script to scrape RedBus data and save it as CSV files.

2. **SQL Integration**:
   - Use the provided SQL schema to create tables.
   - Insert data from the CSV files into the database.

3. **Streamlit App**:
   - Start the app with:
     ```bash
     streamlit run app.py
     ```
   - Navigate through the app to explore bus details interactively.

---

## Features
- **Data Filters**: Search by route, price range, and seat availability.
- **Dynamic Updates**: Real-time filtering and viewing of bus details.
- **Scalable Design**: Easy to add more transport corporations.

---

## Future Improvements
- Add data visualizations for better insights.
- Include a booking link for each bus.
- Implement user authentication for personalized features.

---

## Acknowledgments
- **Selenium**: For seamless data extraction.
- **MySQL**: For robust data storage.
- **Streamlit**: For an elegant user interface.

:)


contact : kishorekumarbn18@gmail.com
