Project Title: Real-Time Stock Dashboard using Streamlit

Description:
This project is a real-time stock dashboard built using Python and Streamlit. The app allows users to track stock prices, display financial metrics, company details, and news articles for a specific ticker on a chosen exchange. It leverages Google Finance and Yahoo Finance APIs to fetch and display data, and it includes features like:

Real-time Stock Metrics: Displays the current stock price, previous close price, and other metrics.
Company Information: Optionally shows revenue, company description, and logo.
Latest News: Fetches and displays the latest 5 news articles related to the stock.
Auto-refresh Functionality: Automatically updates the data every 60 seconds using st_autorefresh.
This project provides a responsive and user-friendly way to monitor financial markets and analyze individual stocks in real time.

🚀 Steps to Clone and Run the Project
Follow these steps to set up and run the project using a virtual environment.

1. Clone the Repository
Open a terminal and run:

git clone https://github.com/sidharth0909/Real-Time-Stock-Dashboard.git
cd Real-Time-Stock-Dashboard

2. Create a Virtual Environment
Create a virtual environment to manage the dependencies locally:
python -m venv venv

3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

4. Install Dependencies
Use the requirements.txt file to install the necessary packages:

pip install -r requirements.txt

5. Run the Application
Start the Streamlit server by running:
streamlit run app.py
