from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, **kwargs):
        super(Type, self).__init__(**kwargs)

    def __repr__(self):
        return "Type<name='%s'>" % (self.name)

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    static = Column(Boolean)

    def __init__(self, **kwargs):
        super(Property, self).__init__(**kwargs)

    def __repr__(self):
        return "Property<name='%s', type='%s', static='%s'>" % (self.name, self.type, self.static)

class Browser(Base):
    __tablename__ = 'browsers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)

    def __init__(self, **kwargs):
        super(Browser, self).__init__(**kwargs)

    def __repr__(self):
        return "Browser<id='%s', name='%s'>" % (self.id, self.name)

class BrowserImplementation(Base):
    __tablename__ = 'browser_implementations'

    id = Column(Integer, primary_key=True)
    browser_name = Column(Integer)
    browser_version = Column(String)

    def __init__(self, **kwargs):
        super(BrowserImplementation, self).__init__(**kwargs)

    def __repr__(self):
        return "Type<browser_name='%s', browser_version='%s'>" % (self.browser_name, self.browser_version)

class Store:
    def __init__(self, path="sqlite:///data.sqlite3"):
        self.engine = create_engine(path, echo=True)
        self.session = sessionmaker(bind=self.engine)
