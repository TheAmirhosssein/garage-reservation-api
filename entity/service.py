from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, relationship

Base = declarative_base()


class Service(Base):
    __tablename__ = "Services"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    duration_minutes = Column(Integer, nullable=False)

    booking = relationship("Booking", back_populates="services")
