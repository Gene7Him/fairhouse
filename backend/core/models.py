from sqlalchemy import Column, Integer, String, Date, Float, DateTime, ForeignKey
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


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    property_id = Column(Integer, ForeignKey("properties.property_id"))
    issue_type = Column(String)
    description = Column(String)
    reporter_name = Column(String)
