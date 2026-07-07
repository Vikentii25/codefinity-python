animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
new_movies = list(animal_movies)
new_movies.append("Dumbo")
new_movies.append("Zootopia")

animal_movies = tuple(new_movies)

print("Updated animal movies:", animal_movies)