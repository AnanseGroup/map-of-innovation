from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

import sqlalchemy
import psycopg2
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils import EmailType

class Innovation_Space(Base):
    __tablename__ = "innovation_space"

    primary_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    aliases = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    phone = Column(String)

    def __repr__(self):
        return "<Innvation_Space(name: %r at street_address: %r and email: %r)>" \
                    % (self.name, self.street_address, self.email)

if __name__ == "__main__":
    #If run as main, reset the engine
    engine = sqlalchemy.create_engine("postgres://lyla@/atlas")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import Session
    import csv
    session = Session(bind=engine)

    with open('most_up-to-date_spaces.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        spaces = [Innovation_Space(name = row['name'],
                                   email = row['email'],
                                   aliases = row['aliases'],
                                   street_address = row['street_address'],
                                   city = row['city'],
                                   state = row['state'],
                                   country = row['country'],
                                   latitude = row['latitude'],
                                   longitude = row['longitude'],
                                   phone = row['phone']) for row in reader]

    #     print(spaces)
        session.add_all(spaces)
        session.commit()