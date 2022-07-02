from fastapi import FastAPI
import services as _services

app = FastAPI()

@app.get("/")
async def root():
    return {'message':'Welcome to this api where you can get quotes from the site: goodreads.com. This Api was made to practice my api development skill and is not intended to be used cormecially'}

@app.get("/quotes")
async def all_quotes():
    return _services.get_all_quotes()

@app.get("/random")
async def random_quote():
    return _services.get_random_quote()