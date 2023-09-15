import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

response = requests.get(URL)
connection = sqlite3.connect("data.db")


def extract(source):
    extracted = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extracted.extract(source)["temperature"]
    return value


def update(temperature):
    cursor = connection.cursor()
    data = (datetime.now(), temperature)
    cursor.execute("INSERT INTO world_temperature VALUES(?,?)", data)
    connection.commit()


if __name__ == "__main__":
    extracted_temp = extract(response.text)
    update(extracted_temp)


