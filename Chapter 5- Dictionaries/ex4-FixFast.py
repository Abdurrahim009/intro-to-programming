rivers = {

    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"

}


for river, country in rivers.items():

    print(f"The {river.capitalize()} runs through {country.capitalize()}.")


print("\nRivers:")

for river in rivers:

    print(river.capitalize())


print("\nCountries:")

for country in rivers.values():
    
    print(country.capitalize())
