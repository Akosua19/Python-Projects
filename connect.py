from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///text_db.db")
session = sessionmaker(bind=engine)()


Base =declarative_base()

class Account(Base):
    __tablename__ = 'Account'


AccountNo = Column(Integer,primary_key=True)
username = column('name', string,unique =True)


def__init__(self,accountno,username):
self.__accountno = accountno
self.__username = username

Base.metadata.create_all(bind=engine)



