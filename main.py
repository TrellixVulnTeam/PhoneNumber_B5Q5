import phonenumbers

Number = "+91 4449508255"

# 3333778888
from phonenumbers import geocoder
ch_number = phonenumbers.parse(Number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service = phonenumbers.parse(Number, "RO")
print(carrier.name_for_number(service, "en"))
