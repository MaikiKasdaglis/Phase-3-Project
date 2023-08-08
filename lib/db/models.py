from sqlalchemy import ForeignKey, Column, Integer, String, Date, MetaData, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///generic')
Session = sessionmaker(bind=engine)
session =Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base()




class Movie(Base):

    __tablename__ = 'movies'
    
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    starring = Column(String())
    rating = Column(String())

    theaters = relationship('Theater', back_populates='movies')

    def __repr__(self):
        return f"{self.id}: {self.title}"

class Theater(Base):

    __tablename__ = 'theaters'
    
    id = Column(Integer(), primary_key=True)
    theater_name = Column(String())
    movie_id = Column(Integer(), ForeignKey('movies.id'))    
    goer_id = Column(Integer(), ForeignKey('goers.id')) 
    city = Column(String())
     
    movies = relationship('Movie', back_populates='theaters')
    goers = relationship('Goer', back_populates='theaters')

    def __repr__(self):
        return f"{self.theater_name}"

class Goer(Base):

    __tablename__ = 'goers'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    
    theaters = relationship('Theater', back_populates='goers')

    def __repr__(self):
        return f"{self.id}: {self.name}" \
            + f"age: {self.age}"