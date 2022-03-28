import bd

from sqlalchemy import Column, Integer, String, Float

class Slangs(bd.Base):
    __tablename__='my_slangs3'

    ID = Column(Integer, primary_key=True,autoincrement=True)
    SLANG= Column(String(50), nullable=False)
    SIGNIFICADO= Column(String(50), nullable=False)

    def __init__(self,ID,SLANG,SIGNIFICADO):
        self.ID = ID
        self.SLANG = SLANG
        self.SIGNIFICADO = SIGNIFICADO

    def __repr__(self):
        return f'\n ID: {self.ID} ||Slang: {self.SLANG}|| Significado: {self.SIGNIFICADO}'
        

    def __str__(self):
        return self.SLANG
