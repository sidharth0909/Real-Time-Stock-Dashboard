import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

st.header('📊 Real-Time Stock Dashboard')

# Sidebar Inputs for Ticker and Exchange
ticker = st.sidebar.text_input('Enter Ticker', 'INFY').upper()
exchange = st.sidebar.text_input('Enter Exchange', 'NSE').upper()

# Validate User Input
if not ticker or not exchange:
    st.warning('Please enter both a ticker and an exchange.')
else:
    # Cache data fetching to improve performance
    @st.cache_data(ttl=60)
    def fetch_stock_data(ticker, exchange):
        """Fetch stock data from Google Finance and Yahoo Finance."""
        url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            # Extract price and previous close
            price = float(soup.find(class_='YMlKec fxKbKc').text.strip()[1:].replace(',', ''))
            previous_close = float(soup.find(class_='P6K39c').text.strip()[1:].replace(',', ''))
        except (AttributeError, ValueError):
            raise ValueError("Error fetching price data.")

        # Extract optional fields
        revenue = soup.find(class_='QXDnM').text.strip() if soup.find(class_='QXDnM') else None
        about = " ".join([item.text for item in soup.find_all(class_='bLLb2d')]) if soup.find_all(class_='bLLb2d') else None

        # Extract news articles
        news = [article.text.strip() for article in soup.find_all('div', class_='Yfwt5')[:5]]

        # Extract company logo
        logo_tag = soup.find('img', {'class': 'img_class_for_logo'})
        logo_url = logo_tag['src'] if logo_tag else None

        return price, previous_close, revenue, about, news, logo_url

    try:
        # Fetch stock data
        price, previous_close, revenue, about, news, logo_url = fetch_stock_data(ticker, exchange)

        # Display financial metrics
        st.metric(label='💰 Current Price', value=f'₹{price}')
        st.metric(label='📉 Previous Close', value=f'₹{previous_close}')

        # Display Company Info if available
        company_info = {}
        if revenue:
            company_info['Revenue'] = revenue
        if about:
            company_info['About'] = about

        if company_info:
            df = pd.DataFrame(company_info, index=['Details']).T
            st.write(df)

        # # Fetch and plot historical data using Yahoo Finance
        # data = yf.download(ticker, period='1mo', interval='1d')
        # st.subheader('📈 Stock Price Trend (Last 1 Month)')
        # if not data.empty:
        #     st.line_chart(data['Close'], height=300, width=700)
        # else:
        #     st.warning("No historical data available.")

        # Display Latest News if available
        if news:
            st.subheader('📰 Latest News')
            for article in news:
                st.write(article)

        # Display Company Logo if available
        if logo_url:
            st.image(logo_url, caption='Company Logo', width=100)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Real-Time Updates (Refresh Every 60 Seconds)
st_autorefresh(interval=60000, key="finance_dashboard")
