'''1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, and then converts that
distance to miles. The conversion formula is as follows:
Miles = Kilometers x 0.6214'''

user_responde_in_km = float(input('Write how many km do you want to convert! '))

def kmConvert(km):
    return format(km*0.6214, ',.2f')

print(kmConvert(user_responde_in_km), ' miles! ')
