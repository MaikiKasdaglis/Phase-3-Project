from models import Movie, Goer, Theater
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('sqlite:///generic.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Movie).delete()
    session.query(Goer).delete()
    session.query(Theater).delete()
    session.commit()

 

    chinese_theatre = Theater(theater_name= 'TCL Chinese Theatre', movie_id =1 ,goer_id = 3, city = 'Los Angeles')

    odeon = Theater(theater_name= 'Odeon Leicester Square', movie_id =2 ,goer_id = 2, city = 'London')

    pvr = Theater(theater_name= 'PVR Cinemas', movie_id =3 ,goer_id = 1, city = 'Mumbai')

    t1 = Theater(theater_name= 'testing', movie_id = 3,goer_id =1 , city = 'la la land')
    
    session.add_all([chinese_theatre, odeon, pvr, t1])
    session.commit()



    barbie = Movie(title = "Barbie", starring = "Margeret Robbie", rating = 2)
    oppenheimer = Movie(title = "Oppenheimer", starring = "Cillian Murphy", rating = 3)
    dark_knight = Movie(title = "The Dark Knight", starring = "Christian Bale", rating = 3)
    session.add_all([barbie, oppenheimer, dark_knight])
    session.commit()

    mark = Goer(name = "Mark", age = 300)
    mike = Goer(name = 'Mike', age = 41)
    cooper = Goer(name = 'Cooper', age = 21)
    session.add_all([mark, mike, cooper])
    session.commit()