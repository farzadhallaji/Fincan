from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
engine = create_engine('sqlite:///views/api_handler/config.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the table schema
class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True)
    exchange = Column(String(50), unique=True)
    key = Column(String(50))
    secret = Column(String(50))

def read_configs():
    session = Session()
    configs = session.query(Config).all()
    session.close()
    return configs

def insert_config(exchange, key, secret):
    configs = read_configs()
    if exchange in [config.exchange for config in configs]:
        update_config(exchange, key, secret)
    else:
        session = Session()
        config = Config(exchange=exchange, key=key, secret=secret)
        session.add(config)
        session.commit()
        session.close()

def update_config(exchange, key, secret):
    session = Session()
    config = session.query(Config).filter_by(exchange=exchange).first()
    if config:
        config.key = key
        config.secret = secret
        session.commit()
    session.close()

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Insert default api key
# insert_config('bybit', 'YWCeoBdf0Y2LqL59TQ', 'R7e2lbwDKXqzlR3bk1wckfmjdCI6vSIfYH2S')