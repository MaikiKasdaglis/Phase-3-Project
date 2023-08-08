from models import (Theater, Movie, Goer)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///generic.db')
Session = sessionmaker(bind=engine)
session = Session()

def print_movies_at_theater():

    theaters = session.query(Theater).all()
    print([theater for theater in theaters])

    selected_theater = input("Select theater: ")
    
    queried_theater = session.query(Theater).filter(Theater.theater_name == selected_theater).first()
    print(f"Theater: {queried_theater}")
    print(f"Movies: {queried_theater.movies}")

def make_movie():

    new_title = input("Enter movie title: ")
    new_star = input("Enter starring actors name: ")
    new_rating = int(input("Enter rating (0=g, 1=pg, 2=pg-13, or 3=R): "))
    new_movie = Movie(title = new_title, starring = new_star, rating = new_rating)
    session.add(new_movie)
    session.commit()

def make_goer():

    new_name = input("Enter name: ")
    new_age = int(input("Enter age: "))
    
    new_goer = Goer(name = new_name, age = new_age)
    session.add(new_goer)
    session.commit()

    
def printMenu(dictionary):
    for i in range(len(dictionary)):
        print(f"{i+1}: {dictionary[i+1].__name__}")
    print(f"{len(dictionary) + 1}: Exit")

def make_theater():

    new_theater_name = input("Enter new theater name: ")
    new_movie_id = int(input("Enter movie id: "))
    new_goer_id = int(input("Goer id: "))
    new_city = input("Enter city: ")

    new_theater = Theater(theater_name = new_theater_name, movie_id = new_movie_id, goer_id = new_goer_id, city = new_city)
    session.add(new_theater)
    session.commit()

function_dict = {1: print_movies_at_theater, 2: make_movie, 3: make_goer, 4: make_theater}

if __name__ == '__main__':

    choice = 0

    while choice != len(function_dict)+1:

        printMenu(function_dict)

        try:
            
            choice = int(input("Enter choice: "))

            if choice < 1 or choice > len(function_dict)+1:

                print("Choice out of range")

            else:
                if choice != len(function_dict)+1:
                    
                    function_dict[choice]()
                
                elif choice == len(function_dict) + 1:
                    break 

        except:

            ValueError("Must enter an integer value!")