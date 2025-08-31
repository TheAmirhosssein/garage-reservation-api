from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, relationship

Base = declarative_base()


class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    addresses = relationship("Address", back_populates="user")

    center = relationship("Center", back_populates="technicians")
    booking = relationship("Booking", back_populates="Technicians")
