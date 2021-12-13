from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = None
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)

class RequestsAmount(BaseModel):
    __tablename__ = 'requests_amount'

    Requests_amount = Column(Integer, nullable=False)


class RequestsByType(BaseModel):
    __tablename__ = 'requests_by_type'

    Request_method = Column(String(10), nullable=False)
    Requests_amount = Column(Integer, nullable=False)


class Top10MostFrequent(BaseModel):
    __tablename__ = 'top10_most_frequent'

    Url = Column(String(100), nullable=False)
    Requests_amount = Column(Integer, nullable=False)


class Top5Err5xx(BaseModel):
    __tablename__ = 'top5_5xx_err'

    IP = Column(String(30), nullable=False)
    Requests_amount = Column(Integer, nullable=False)


class Top5Err4xx(BaseModel):
    __tablename__ = 'top5_4xx_err'

    Url = Column(String(500), nullable=False)
    Status_code = Column(Integer, nullable=False)
    Url_size = Column(Integer, nullable=False)
    IP = Column(String(30), nullable=False)
