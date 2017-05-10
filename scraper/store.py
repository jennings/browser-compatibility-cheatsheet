from contextlib import contextmanager
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_Base = declarative_base()

class Type(_Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    page_text = Column(String)

    def __init__(self, **kwargs):
        super(Type, self).__init__(**kwargs)

    def __repr__(self):
        return "Type<name='%s'>" % (self.name)

class Property(_Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    static = Column(Boolean)

    def __init__(self, **kwargs):
        super(Property, self).__init__(**kwargs)

    def __repr__(self):
        return "Property<name='%s', type='%s', static='%s'>" % (self.name, self.type, self.static)

class Browser(_Base):
    __tablename__ = 'browsers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)

    def __init__(self, **kwargs):
        super(Browser, self).__init__(**kwargs)

    def __repr__(self):
        return "Browser<id='%s', name='%s'>" % (self.id, self.name)

class BrowserImplementation(_Base):
    __tablename__ = 'browser_implementations'

    id = Column(Integer, primary_key=True)
    browser_name = Column(Integer)
    browser_version = Column(String)

    def __init__(self, **kwargs):
        super(BrowserImplementation, self).__init__(**kwargs)

    def __repr__(self):
        return "Type<browser_name='%s', browser_version='%s'>" % (self.browser_name, self.browser_version)

_engine = create_engine("sqlite:///data.sqlite3")
_Base.metadata.create_all(_engine)
_Session = sessionmaker(bind=_engine)

@contextmanager
def Session():
    session = _Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
