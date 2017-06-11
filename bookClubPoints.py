'''11. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 2 books, he or she earns 5 points.
Programming Exercises 135
• If a customer purchases 4 books, he or she earns 15 points.
• If a customer purchases 6 books, he or she earns 30 points.
• If a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has purchased
this month and displays the number of points awarded.'''
pointsEarned = 0
books_bought= int(input('How much costumer bought? '))
if books_bought==2:   pointsEarned+=5
elif books_bought==4: pointsEarned+=15
elif books_bought==6: pointsEarned+=30
elif books_bought>=8: pointsEarned+=60

print('Customer bought', books_bought, 'book(s) and earned', pointsEarned, 'points!', sep=' ')