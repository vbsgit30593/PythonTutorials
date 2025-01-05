from ast import Assign
from typing import NamedTuple

class City(NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]

def matchCities():
    asianCountries = {}
    for city in cities:
        match city:
            case City(continent='Asia', name=name, country=country):
                asianCountries[name] = country

            case City('North America', name=name, country=country):
                asianCountries[name] = country

            case _:
                asianCountries["Noname"] = "nocountry"

    print (f'{"Name":15} | {"Country":>15}')
    for name, country in asianCountries.items():
        print (f'{name:15} | {country:>15}')

    print (City.__match_args__)

matchCities()