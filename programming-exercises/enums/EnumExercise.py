import enum
from enum import Enum, IntEnum

class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
    India = 355
    USA = 213

print("Member Name: {}".format(Country.Albania.name))
print("Member Value: {}".format(Country.Albania.value))

for data in Country:
   print("{:15} = {}".format(data.name, data.value))

print("Country name ordered by country code")
print('\n'.join('  ' + c.name for c in sorted(Country)))

country_code_list = list(map(int,Country))
print(country_code_list)

for result in Country:
    print("{:15} = {}".format(result.name, result.value))