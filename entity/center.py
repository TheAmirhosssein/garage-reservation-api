from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, relationship

Base = declarative_base()


class Center(Base):
    __tablename__ = "centers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    technicians = relationship("Technician", back_populates="centers")
    booking = relationship("Booking", back_populates="centers")
