import sqlalchemy
import psycopg2
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType

Base = declarative_base()
engine = create_engine("postgres://lyla@/atlas")
Base.metadata.bind = engine

class Innovation_Space(Base):
    __tablename__ = "innovation_space"
    __table__ = Table(__tablename__, Base.metadata, autoload=True)

    # primary_id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String)
    # email = Column(String)
    # aliases = Column(String)
    # street_address = Column(String)
    # city = Column(String)
    # state = Column(String)
    # country = Column(String)
    # latitude = Column(Float, nullable=True)
    # longitude = Column(Float, nullable=True)
    # phone = Column(String)

    def __repr__(self):
        return "<Innovation_Space(name: %r at street_address: %r and email: %r)>" \
                    % (self.name, self.street_address, self.email)

    _column_names_list = None
    def _column_names(self):
      if not self._column_names_list:
        self._column_names_list = [x.__str__().split('.')[1] for x in self.__table__.columns]
      return self._column_names_list


    def __json__(self):
        return { column: getattr(self, column) for column in self._column_names() }

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    import csv
    import inspect
    #If run as main, reset the engine
    engine = sqlalchemy.create_engine("postgres://lyla@/atlas")

    def dynamic_space_schema():
        with open('most_up-to-date_spaces.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for key in reader.__next__().keys():
                if not getattr(Innovation_Space, key, None):
                    setattr(Innovation_Space, key, Column(String))
    dynamic_space_schema()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    session = Session(bind=engine)
    with open('most_up-to-date_spaces.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        spaces = [{key: value if not value == '' else None for key, value in row.items()} for row in reader]
        spaces = [Innovation_Space(**space) for space in spaces]
        session.add_all(spaces)
        session.commit()
    session.close()
