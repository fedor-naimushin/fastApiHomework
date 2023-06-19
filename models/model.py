from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Metadata = MetaData()


class Roles(Base):
    __tablename__ = 'Roles'
    metadata = Metadata
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class Users(Base):
    __tablename__ = 'Users'
    metadata = Metadata
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    roles_id = Column(Integer, ForeignKey(f'{Roles.id}'))