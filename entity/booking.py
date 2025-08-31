from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(50), nullable=False)
    booking_type = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)

    center = relationship("Center", back_populates="bookings")
    technician = relationship("Technician", back_populates="bookings")
    service = relationship("Service", back_populates="bookings")
