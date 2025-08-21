import pandas as pd
import yfinance as yf

# Mapping of organisation names to stock ticker symbols
ORG_TICKER_MAP = {
    "Twitter": "TWTR",
    "Facebook": "META",
    "Linkedin": "MSFT",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Google+": "GOOGL",
    "Yahoo": "AABA",  # Yahoo ticker (now Altaba, historical)
    "Uber": "UBER",
    "Marriott International": "MAR",
    "British Airways": "IAG.L",  # London Stock Exchange
    "T-Mobile": "TMUS",
    "Equifax": "EFX",
    "Cathay Pacific Airways": "0293.HK",
    "Dell": "DELL",
    "Nvidia": "NVDA",
    "Spotify": "SPOT",
    "Tesla": "TSLA",
    "PayHere": "",  # Not public
    "Heroku": "",   # Owned by Salesforce (CRM)
    "Mailchimp": "", # Not public
    "Robinhood": "HOOD",
    "GoDaddy": "GDDY",
    "VW": "VOW3.DE",
    "MacDonalds": "MCD",
    "Air India": "", # Not public
    "Peloton": "PTON",
    "Digital Ocean": "DOCN",
    "Park Mobile": "", # Not public
    "Ubiquiti": "UI",
    "Meet Mindful": "", # Not public
    "Experian SA": "EXPN.L",
    "Gab": "", # Not public
    "Star Alliance": "", # Not public
    "Ledger": "", # Not public
    "The Hospital Group": "", # Not public
    "SolarWinds": "SWI",
    "Ho Mobile": "", # Owned by Vodafone (VOD)
    "Drizly": "", # Owned by Uber (UBER)
    "Nintendo": "NTDOY",
    "Pakistani mobile operators": "", # Not public
    "US Marshals Service": "", # Not public
    "EasyJet": "EZJ.L",
    "Microsoft": "MSFT",
    "Virgin Media": "", # Owned by Liberty Global (LBTYA)
    "Tesco Clubcard": "TSCO.L",
    "Marriott Hotels": "MAR",
    "Zoom": "ZM",
    "Israeli government": "",
    "MGM Hotels": "MGM",
    "Wawa": "", # Not public
    "Desjardins Group": "", # Not public
    "Quest Diagnostics": "DGX",
    "Canva": "", # Not public
    "Toyota": "TM",
    "Facebook": "META",
    "DoorDash": "DASH",
    "Capital One": "COF",
    "Dell": "DELL",
    "Apple": "AAPL",
    "Google+": "GOOGL",
    "Amazon": "AMZN",
    "Uber": "UBER",
    "Linkedin": "MSFT",
    "Twitter": "TWTR",
    "Yahoo": "AABA",
    "Nvidia": "NVDA",
    "Spotify": "SPOT",
    "Robinhood": "HOOD",
    "GoDaddy": "GDDY",
    "VW": "VOW3.DE",
    "MacDonalds": "MCD",
    "Peloton": "PTON",
    "Digital Ocean": "DOCN",
    "Ubiquiti": "UI",
    "Experian SA": "EXPN.L",
    "SolarWinds": "SWI",
    "Nintendo": "NTDOY",
    "EasyJet": "EZJ.L",
    "Microsoft": "MSFT",
    "Tesco Clubcard": "TSCO.L",
    "Marriott Hotels": "MAR",
    "Zoom": "ZM",
    "MGM Hotels": "MGM",
    "Quest Diagnostics": "DGX",
    "Toyota": "TM",
    "DoorDash": "DASH",
    "Capital One": "COF",
    # Add more mappings as needed
}

def get_stock_price(ticker):
    if not ticker:
        return None
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close']
        if not price.empty:
            return price.iloc[0]
        else:
            return None
    except Exception:
        return None

# Load breaches data
breaches_df = pd.read_csv('Balloon Race Data Breaches - LATEST - breaches.csv')

# Clean up organisation names for mapping
def clean_org_name(name):
    if isinstance(name, str):
        return name.strip().replace('"', '')
    return name

breaches_df['organisation_clean'] = breaches_df['organisation'].apply(clean_org_name)
breaches_df['Ticker'] = breaches_df['organisation_clean'].map(ORG_TICKER_MAP)

# Fetch stock prices
breaches_df['Stock Price'] = breaches_df['Ticker'].apply(get_stock_price)

# Select relevant columns for output
output_df = breaches_df[['organisation', 'records lost', 'year   ', 'Ticker', 'Stock Price']]

# Save to CSV
output_df.to_csv('breaches_with_stock_prices.csv', index=False)