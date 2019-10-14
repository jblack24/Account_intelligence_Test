from sqlalchemy import create_engine
import sqlalchemy.orm as orm
from config import Config
from sqlalchemy.ext.declarative import declarative_base

Session=orm.sessionmaker()
engine=create_engine(Config.engine_url, echo=True)
Session.configure(bind=engine)
session=Session()
Base=declarative_base()
