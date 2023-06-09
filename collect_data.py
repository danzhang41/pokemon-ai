"""
(1) Generate a list of matches to collect.
(2) Download the matches using public APIs.
(3) Parse data.
(4) Store in a csv file.
"""
import requests
import json
import copy

from config import FORMAT, POKEMON_SHOWDOWN

def apiCall(url: str) -> dict:
    """
    Get json data from API call.
    Example URL https://replay.pokemonshowdown.com/gen8doublesubers-1097585496.json
    """
    data = {}
    try:
        response = requests.get(url)
        data = json.loads(response.text)
    except:
        print(f"Could not load json data from {url}")
    return data

def formatUrlArgs(base_url: str, args: dict) -> str:
    """
    Adds arguments to url.
    Assumes base url does not have args already.

    Example:
    base_url = https://replay.pokemonshowdown.com/search.json
    args={"user": "zarel", "page": 2}

    https://replay.pokemonshowdown.com/search.json?user=zarel&page=2
    """
    assert "?" not in base_url

    args_str = ""
    for arg in args:
        args_str += f"&{arg}={args[arg]}"
    args_str = "?" + args_str[1:]
    return base_url + args_str

def getMostRecentMatchesFormat(format: str = None, args=None) -> list:
    """Return a JSON formatted list of matches by format """
    if format is None:
        format = FORMAT
    if args is None:
        args = {}

    args = copy.deepcopy(args)
    args.update({"format": format})

    url = formatUrlArgs(base_url=POKEMON_SHOWDOWN, args=args)
    return apiCall(url=url)

def saveReplay():
    j = apiCall("https://replay.pokemonshowdown.com/gen9vgc2023series2-1829661013.json")
    with open("klfsf.txt", "w+") as f:
        json.dump(j, f, indent=4)
    print(j["log"])


if __name__ == '__main__':
    result = getMostRecentMatchesFormat()
    saveReplay()
    