import json
from random import randint
from os import system

def game() -> dict:
    secret_number = randint(1, 100)
    guesses = 1
    system("cls")
    while True:
        try:
            guess = int(input("Gissning: "))
        except TypeError:
            system("cls")
            print("Svar måste vara siffra")
            continue
        if guess > secret_number:
            system("cls")
            print("För högt")
        elif guess < secret_number:
            system("cls")
            print("För lågt")
        else:
            system("cls")
            print("Rätt")
            break
        guesses += 1
    return {
        "name": input("Namn: "),
        "guesses": guesses
    }

def load_file():
    global scoreboard
    with open(FILENAME, "r", encoding="utf-8") as file:
        scoreboard = json.load(file)

def save_file(scores: list):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4, ensure_ascii=False)

FILENAME = "highscores.json"

try:
    load_file()
except FileNotFoundError:
    save_file([])
    load_file()
for score in range(3):
    try:
        print(f"{scoreboard[score]["name"]}: {scoreboard[score]["guesses"]}")
    except IndexError:
        break
input("Tryck [ENTER] för att fortsätta")
scoreboard.append(game())
scoreboard.sort(key=lambda item: item["guesses"])
try:
    del scoreboard[5]
except IndexError:
    print(end="")
save_file(scoreboard)