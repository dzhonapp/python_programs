'''6. Calories from Fat and Carbohydrates
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams x 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams x 4
The nutritionist asks you to write a program that will make these calculations.'''

fat_grams = float(input('What amount of fat you consume daily? '))
carb_grams = float(input('What amount of carbs you consume daily? '))

def calculate_calories(fat, carbs):
    print("daily calories from fat: ", format(fat*9, ',.2f'))
    print("Daily calories from carbs: ", format(carbs*4, ',.2f') )


calculate_calories(fat_grams, carb_grams)
