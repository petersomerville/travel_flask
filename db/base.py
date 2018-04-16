from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()
DB_FILE = 'sqlite:///db/DATABASE.sqlite'


def inverse_relationship(tablename):
    return backref(tablename, uselist=True, cascade='delete, all, delete-orphan', lazy='dynamic')


def get_session():
    engine = create_engine(DB_FILE)
    sesson_config = sessionmaker(bind=engine, expire_on_commit=False)
    Base.metadata.create_all(engine)
    return sesson_config()


def create_db():
    engine = create_engine(DB_FILE)
    Base.metadata.create_all(engine)

def create_tables():
    get_session().close()     


class DbManager:
    
    def __init__(self):
        self.session = None
        self.is_transactional = False

    def commit(self):
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise
        
    def begin(self):
        self.is_transactional = True
        return self.open()

    def end(self):
        self.is_transactional = False
        self.commit()
        self.close()

    def open(self):
        if self.session is None:
            self.session = get_session()
        return self.session

    def close(self):
        if self.session is not None:
            self.is_open = False
            self.session.expunge_all()
            self.session.close()
            self.session = None

    def save(self, obj):
        self.open()
        self.session.add(obj)
        if not self.is_transactional:
            self.commit()
        return obj

    def delete(self, obj):
        self.open()
        self.session.delete(obj)
        if not self.is_transactional:
            self.commit()
        return obj

    def update(self, obj):
        self.open()
        if not self.is_transactional:
            self.commit()
        return obj

if __name__ != '__main__':
    create_db()