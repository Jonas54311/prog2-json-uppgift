import json

FILENAME = "user_config.json"

def load_file():
    global user_info
    with open(FILENAME, "r", encoding="utf-8") as file:
        user_info = json.load(file)

def save_file(info: dict):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=4, ensure_ascii=False)

try:
    load_file()
    print(f"Välkommen tillbaka {user_info["name"]}! Du har startat programmet {user_info["visits"]} gånger")
except FileNotFoundError:
    save_file({"name": input("name: "), "visits": 0})
    load_file()
    print(f"Välkommen {user_info["name"]}")

user_info["visits"] += 1
save_file(user_info)