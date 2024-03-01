current_movies = {"Oppenheimer": "12:00pm",
                  "Barbie": "5:00pm",
                  "The Holdovers": "8:00pm",
                  "The Zone of Interest": "10:00pm"}

print(current_movies)

# Practice adding pairs to dictionary
current_movies["Anatomy of a Fall"] = "7:00pm"
print(current_movies)

current_movies.update({"The Society of the Snow": "10:00am"})
print(current_movies)

# Practice updating values
current_movies["Barbie"] = "4:00pm"
print(current_movies)

# Print the movies with a for loop and ask for user input
print("We are showing the following movies:")
for key in current_movies:
    print(key)

user_movie = input("Which movie do you want to the showtime for?\n")

showtime = current_movies.get(user_movie)

if showtime == None:
    print("We are not showing that movie")
else:
    print(user_movie, "is shown at", showtime)
