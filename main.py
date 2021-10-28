from phonenumbers import geocoder
import phonenumbers
import opencage
import folium


filename = "sample_name_rick"
number = "+639162262994"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = '4f1fee3798d34ae88836be965af7e14e'

geocode = OpenCageGeocode(key)
query = str(location)
results = geocode.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)


myMap.save("{}.html".format(filename))
