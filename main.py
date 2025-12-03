# app.py
import typer
import requests
from dotenv import load_dotenv
import os

load_dotenv() 

app = typer.Typer()

base_script = """

def solution(file):
    pass

with open("input.txt", 'r') as file:
    solution(file)    

"""


url = "https://adventofcode.com/"


def get_input(year, day):
    cookies = {
        "session": os.getenv("SESSION_KEY"),
    }

    headers = {
        "Content-Type": "application/json"
    }

    new_url = url + str(year) + "/day/" + str(day) + "/input"
    response = requests.post(new_url, headers=headers, cookies=cookies)
    return response.text

@app.command()
def create(year: int, num: int):
    day = "day-" + str(num) + '/'
    os.makedirs("day-" + str(num), exist_ok=True)
    with open(day + 'part-1.py', 'w') as file:
        file.write(base_script)
    with open(day + 'part-2.py', 'w') as file:
        file.write(base_script)
    with open(day + "input.txt", "w") as file:
        file.write(get_input(year, num))

   


if __name__ == "__main__":
    app()

