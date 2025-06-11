from fastapi import FastAPI, Header, Cookie
from fastapi.responses import JSONResponse
from typing import Annotated
import requests
import math
import random

app = FastAPI()
host = 'http://127.0.0.1:8080'

def print_menu():
    print("\n")
    print("The following numbers relate to a path, select a number to run that path")
    print("1. Get User Agent (GET Headers) ")
    print("2. Enter Your Age (GET Headers) ")
    print("3. Calculate 2 numbers (GET Headers) ")
    print("4. Play Rock Paper Scissors (GET Headers) ")
    print("5. Enter your age (POST Cookies) ")
    print("6. Calculate 2 numbers (POST Cookies) ")
    print("7. Play Rock Paper Scissors (POST Cookies) ")
    print("8. Exit")
    print("\n")

async def calculate(num1: int, num2: int, operation: str):
    operation = operation.upper()

    match operation:
        case 'ADD':
            return f'{num1} + {num2} = {num1 + num2}'
        case 'SUBTRACT':
            return f'{num1} - {num2} = {num1 - num2}'
        case 'MULTIPLY':
            return f'{num1} x {num2} = {num1 * num2}'
        case 'DIVIDE':
            return f'{num1} ÷ {num2} = {num1 / num2}'
        
async def rps(choice: str):
    options = ['ROCK', 'PAPER', 'SCISSORS']
    index = math.floor(random.uniform(0, 3)) - 1
    comp = options[index]

    # 0 = draw, 1 = win, 2 = loss
    user_win = 0
    choice = choice.upper()
    
    if (choice == 'ROCK' or choice == 'PAPER' or choice == 'SCISSORS'):
        match choice:
            case 'ROCK':
                if (comp == 'ROCK'):
                    user_win = 0
                if (comp == 'SCISSORS'):
                    user_win = 1
                if (comp == 'PAPER'):
                    user_win = 2
            case 'PAPER':
                if (comp == 'ROCK'):
                    user_win = 1
                if (comp == 'SCISSORS'):
                    user_win = 2
                if (comp == 'PAPER'):
                    user_win = 0
            case 'SCISSORS':
                if (comp == 'ROCK'):
                    user_win = 2
                if (comp == 'SCISSORS'):
                    user_win = 0
                if (comp == 'PAPER'):
                    user_win = 1

        result = 'result'

        match user_win:
            case 0:
                result = f'Computer chose {comp}, draw!'
            case 1:
                result = f'Computer chose {comp}, you win!'
            case 2:
                result = f'Computer chose {comp}, you lose!'
        
        return result
    
    return "Enter a valid option!"

@app.get("/user_agent")
async def get_agent(user_agent: Annotated[str | None, Header()]):
    return {"User-Agent": user_agent}

@app.get("/age_headers")
async def read_items(age: Annotated[int | None, Header()] = None):
    return {"age": age}

@app.get("/calculate_headers")
async def calculate_nums(
    num1: Annotated[int | None, Header()] = None,
    num2: Annotated[int | None, Header()] = None,
    operation: Annotated[str | None, Header()] = None):
    return { "answer": await calculate(num1, num2, operation) }

@app.get("/play_rps_headers")
async def play_rps(
    choice: Annotated[str | None, Header()] = None
):
    return { "result": await rps(choice) }

@app.post("/age_cookies")
async def post_age(age: Annotated[str | None, Cookie()] = None):
    return { "age": age }

@app.post("/calculate_cookies")
async def post_calculate(
    num1: Annotated[int | None, Cookie()] = None,
    num2: Annotated[int | None, Cookie()] = None,
    operation: Annotated[str | None, Cookie()] = None
):
    return { "answer": await calculate(num1, num2, operation) }

@app.post("/play_rps_cookies")
async def play_rps(
    choice: Annotated[str | None, Cookie()] = None
):
    return { "result": await rps(choice) }

def maindriver():

    continueLoop = True
    while continueLoop:
        
        print_menu()
        choice = int(input('Enter a number: '))

        match choice:
            case 1:
                response = requests.get(host + "/user_agent")
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(response.status_code)

            case 2:
                age = int(input("Enter your age: "))
                headers = { "age": str(age) }

                response = requests.get(host + "/age_headers", headers=headers)
                if (response.status_code == 200):
                    print(response.json())
                else:
                    print(response.status_code)
            
            case 3:
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                operation = input("Enter your operation (add, subtract, multiply, divide): ")
                headers = {
                    "num1": str(num1),
                    "num2": str(num2),
                    "operation": operation
                }

                response = requests.get(host + "/calculate_headers", headers=headers)
                if (response.status_code == 200):
                    print(response.json())
                else:
                    print(response.status_code)
            
            case 4:
                choice = input("Choose Rock, Paper or Scissors: ")
                headers = { "choice": choice }

                response = requests.get(host + "/play_rps_headers", headers=headers)
                if (response.status_code == 200):
                    print(response.json())
                else:
                    print(response.status_code)

            case 5:
                age = int(input("Enter your age: "))
                cookies = { "age": str(age) }

                response = requests.post(host + "/age_cookies", cookies=cookies)
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(response.status_code)

            case 6:
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                operation = input("Enter your operation(add, subtract, multiply, divide): ")
                cookies = {
                    "num1": str(num1),
                    "num2": str(num2),
                    "operation": operation
                }

                response = requests.post(host + "/calculate_cookies", cookies=cookies)
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(response.status_code)

            case 7:
                choice = input("Choose Rock, Paper or Scissors: ")
                cookies = { "choice": choice }

                response = requests.post(host + "/play_rps_cookies", cookies=cookies)
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(response.status_code)
            case _:
                print("Exiting...")
                continueLoop = False
        

if __name__ == "__main__":
    maindriver()
