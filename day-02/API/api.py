import requests
import config
import json

api_key = config.api_key   # Accessing the API key from config.py

joke_url = "https://official-joke-api.appspot.com/random_joke"

market_stack_url = f"https://api.marketstack.com/v2/eod?access_key={api_key}"

store_info = r"C:\Users\Abhinav Private\Documents\Python Study\python-for-devops\day-02\API\output.txt"

def mood_check(mood, symbol=None):

    if mood.lower() == "joke":
        response = requests.get(url=joke_url)
        # print(json.dumps(response.json(), indent=4))
        print(f"{response.json()['setup']},\n{response.json()['punchline']}")
    
    
    elif mood.lower() == "market_stack":
        response = requests.get(url=market_stack_url + f"&symbols={symbol}")
        
        with open(store_info, "w") as file:    
            file.write(json.dumps(response.json(), indent=4))
        
        print(json.dumps(response.json(), indent=4))
    
    
    else:
        print("Mood not recognized. Please enter 'Joke' or 'market_stack'.")

mood = input("what is your mood? example: Joke, market_stack: ")
symbol = None
if mood.lower() == "market_stack":
    symbol = input("Enter stock symbol. example: AAPL, MSFT: ")

mood_check(mood, symbol)

