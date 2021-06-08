import phonenumbers

import folium

from tracknumber import number

from phonenumbers import geocoder

Key = '90a65aa9486c4df9acb400d89198da38'

samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

#get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)

##print (results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

##map html

myMap.save("Location.html")

##finish -p