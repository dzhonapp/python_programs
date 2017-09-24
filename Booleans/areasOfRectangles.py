'''2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same.
'''


r1 = float(input("WHat is the length of rectangle 1 ? "))
r1width = float(input("What is the width of rectangle 1? "))

r2 = float(input("WHat is the length of rectangle 2 ? "))
r2width = float(input("What is the width of rectangle 2? "))
z = r1 * r1width if r1*r1width > r2*r2width else r2*r2width
print(z)