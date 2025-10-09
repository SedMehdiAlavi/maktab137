import json
from idlelib.config import InvalidConfigType, InvalidConfigSet
from json import JSONDecodeError

#part1
class InvalidConfigError(Exception):
    def __init__(self, message):
        self.message = message
        print(f"{self.message}")

#part2,3
def load_config(filepath):

    try:

        with open(filepath) as file:
            dict = json.load(file)

            if "api_key" not in dict:
                raise InvalidConfigError("api_key is missing")

            elif "database_url" not in dict:
                raise InvalidConfigError("database_url is missing")

            elif "mode" not in dict:
                raise InvalidConfigError("mode is missing")

        with open(filepath) as file:
            dict = json.load(file)

            if dict["mode"] != "debug" and dict["mode"] != "production":
                raise InvalidConfigError("mode is invalid")

            else:
                print("Every thing is OK")

    except FileNotFoundError:
        print("Error : FileNotFoundError")

    except JSONDecodeError:
        print("Error : JSONDecodeError")

#part4
try:
    load_config("config.json")

except FileNotFoundError:
    print("Error : config.json Not Found!")

except JSONDecodeError:
    print("Error : Invalid JSON!")

except InvalidConfigError:
    print("Error : Invalid Config!")

except InvalidConfigSet:
    print("Error : Invalid Config Set!")

except InvalidConfigType:
    print("Error : Invalid Config Type!")