
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#TODO: Create Engine
#TODO :create session
#TODO: Access Sqlite with that seesion and write data to that engine

class Session:

    def __init__(self,db_path:str):
        self.db_path=db_path
        self.create_engine()
        self.create_session()

    def create_engine(self):
        db_url=f'sqlite:///{self.db_path}'
        self.engine = create_engine(db_url,echo=True)

    def create_session(self):
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_engine(self):
        return self.engine
    
    def get_session(self):
        return self.SessionLocal()       
    
    
