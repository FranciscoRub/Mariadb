from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///my_slangs3.db')
engine = create_engine('mysql+pymysql://root:Winston25root@localhost/my_slangs3')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
