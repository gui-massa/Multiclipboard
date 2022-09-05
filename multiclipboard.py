from ast import Pass
from curses import keyname
import sys
import clipboard
import json

SAVED_DATA = "multiclipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except: 
        return {}


def list_data(filepath):
    with open(filepath, "r") as f:
        for key in f:
            print(key)


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ") #substituir usando sys.argb[3] -> dessa forma adicionando a key no pedido
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
        else:
            raise KeyError("Chave inexistente.")

    elif command == "list":
        print("até aqui ok")
        list_data(SAVED_DATA)

else:
    print("Did you mean: ")
    print("python3 multiclipboard.py save --> Save what is on clipboard to json on a key")
    print("python3 multiclipboard.py load --> Load what is on a specific json key")
    print("python3 multiclipboard.py list --> List all that is saved")


