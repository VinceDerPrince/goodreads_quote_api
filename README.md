# Goodreads.com Popular Quotes API
An API to get the populart quotes from the site ![goodreads](https://www.goodreads.com/quotes).

## Features
You can get:
* All popular quotes:
![All quotes](/images/all_quotes.gif)
* All popular quotes from a specific name:
![Quotes by name](/images/qutoe_by_name.gif)
* All popular quotes under a specific tag:
![Quotes by tag](/images/quote_by_tag.gif)
* A random popular quote:
![Random Quote](/images/random_quote.gif)

## Setup
### Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
Or use any virtual environment you like.

### Uvicorn
To show the UI I used in the Introduction, we use uvicorn.
You do this as such:
```
uvicorn main:app --reload
```
It should know look like this in your terminal and a browser Window with the API UI should show up.

![Uvicorn Setup](/images/uvicorn_setup.png)