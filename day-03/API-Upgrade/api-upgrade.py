import requests
import json
import os
import logging
import datetime
import time

# Set up basic logging
logging.basicConfig(level=logging.ERROR, 
                    filename='app.log', 
                    filemode='a',
                    format=f'{datetime.datetime.fromtimestamp(time.time(), tz=datetime.timezone.utc)} - %(levelname)s - %(message)s')
                    
try:
    import config
    API_KEY = config.api_key
except ImportError:
    logging.error("config.py not found or api_key not defined.")
    exit(1)
except AttributeError:
    logging.error("api_key not found in config.py.")
    exit(1)

# Constants
JOKE_URL = "https://official-joke-api.appspot.com/random_joke"
MARKET_STACK_BASE_URL = f"https://api.marketstack.com/v2/eod?access_key={API_KEY}"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "output.txt")

def fetch_joke():
    """Fetch and print a random joke."""
    try:
        response = requests.get(JOKE_URL)
        response.raise_for_status()
        data = response.json()
        print(f"{data['setup']},\n{data['punchline']}")
    except requests.RequestException as e:
        logging.error(f"Error fetching joke: {e}")
        print("Failed to fetch joke. Please try again.")
    except KeyError:
        logging.error("Unexpected joke API response format.")
        print("Invalid joke response.")

def fetch_market_data(symbol):
    """Fetch market data for a symbol and save/print it."""
    if not symbol or not symbol.isalpha():
        print("Invalid stock symbol. Please enter a valid one (e.g., AAPL).")
        return
    
    url = f"{MARKET_STACK_BASE_URL}&symbols={symbol.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Write to file
        with open(OUTPUT_FILE, "w") as file:
            json.dump(data, file, indent=4)
        
        print(json.dumps(data, indent=4))
    except requests.RequestException as e:
        logging.error(f"Error fetching market data: {e}")
        print("Failed to fetch market data. Check your API key and symbol.")
    except (json.JSONDecodeError, KeyError):
        logging.error("Unexpected market API response format.")
        print("Invalid market data response.")

def mood_check(mood, symbol=None):
    """Check mood and call appropriate function."""
    mood = mood.lower().strip()
    if mood == "joke":
        fetch_joke()
    elif mood == "market_stack":
        fetch_market_data(symbol)
    else:
        print("Mood not recognized. Please enter 'joke' or 'market_stack'.")

# Main execution
mood = input("What is your mood? Example: joke, market_stack: ").strip()
symbol = None
if mood.lower() == "market_stack":
    symbol = input("Enter stock symbol. Example: AAPL, MSFT: ").strip()

mood_check(mood, symbol)

