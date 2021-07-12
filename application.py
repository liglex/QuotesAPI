#open('test.json', encoding='utf-8-sig')

from flask import  Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_quotes():
    r = requests.get('https://www.breakingbadapi.com/api/quote/random')
    quotes = r.json()
    print(quotes)
    quote = next(item for item in quotes if item['quote'])
    print(quote)
    text = quote.get('quote')
    print(text)
    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
