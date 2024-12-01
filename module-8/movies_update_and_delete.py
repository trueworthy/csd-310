# Lea Trueworthy
# November 25, 2024
# CSD 310 - Module 8.2 Assignment: Movies: Update & Deletes
# Description: Create a Python file named movies_update_and_delete.py. Connect to the movies database and use show_films(cursor, "DISPLAYING FILMS") to display the films.
    # Insert a new film (not 'Star Wars'), then update "Alien" to a Horror film and delete "Gladiator."
    # Use show_films after each change to display the updated list.

import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Establish the connection to the database
db_connection = mysql.connector.connect(**config)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# The provided function to show films
def show_films(cursor, title):
    # Execute an inner join query to get the required data
    cursor.execute('''SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
                      FROM film 
                      INNER JOIN genre ON film.genre_id = genre.genre_id 
                      INNER JOIN studio ON film.studio_id = studio.studio_id''')
    
    # Fetch all the results from the executed query
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    # Display each film's details
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Use the show_films function to display the films in the database
show_films(cursor, "-- DISPLAYING FILMS --")

# Insert a new film into the film table
insert_query = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) " \
                   "VALUES ('Serenity', '2005', '119', 'Joss Whedon', (SELECT studio_id FROM studio WHERE " \
                  "studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') ); "

cursor.execute(insert_query)
db_connection.commit()

# Display films after inserting
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

# Update the genre of "Alien" to Horror
update_query = "update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where " \
                  "film_name = 'Alien'; "

cursor.execute(update_query)
db_connection.commit()

# Display films after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")

# Delete the movie "Gladiator"
delete_query = " DELETE FROM film WHERE film_name = 'Gladiator';"

cursor.execute(delete_query)
db_connection.commit()

# Display films after deleting
show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

# close the cursor and connection
cursor.close()
db_connection.close()
