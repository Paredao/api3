from sqlalchemy import Column, Integer, String
from database import Base

class Ip(Base):
    __tablename__="ips"

    