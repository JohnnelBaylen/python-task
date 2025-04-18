rating = float(input("Enter the rating : "))

if rating >= 4.5:
    print("Entraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")