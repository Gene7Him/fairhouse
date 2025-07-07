from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    property_id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    zip_code = Column(String)
    owner_name = Column(String)
    last_sale_price = Column(Integer)
    sale_date = Column(Date)
    accountability_score = Column(Float)
