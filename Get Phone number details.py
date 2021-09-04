import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Inter mobile number whith country code:
mobileNumb = input('Введите номер телефона с кодом страны')
mobileNumb = phonenumbers.parse(mobileNumb)

# Get time zone a phone number
print(timezone.time_zones_for_number(mobileNumb))

# Getting carrier of a phone number
print(carrier.name_for_number(mobileNumb, 'ru'))

# Getting region information
print(geocoder.description_for_number(mobileNumb, 'ru'))

# Validating a phone number
print('Номер валидный: ', phonenumbers.is_valid_number(mobileNumb))

# Checking possibility of number
print('Проверка доступности номера: ', phonenumbers.is_possible_number(mobileNumb))