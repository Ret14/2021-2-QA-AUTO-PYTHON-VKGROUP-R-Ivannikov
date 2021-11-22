from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# class Prepod(Base):
#     __tablename__ = 'prepods'
#     __table_args__ = {'mysql_charset': 'utf8'}
#
#     def __repr__(self):
#         return f"<Prepod(" \
#                f"id='{self.id}'," \
#                f"name='{self.name}', " \
#                f"surname='{self.surname}', " \
#                f"start_teaching='{self.start_teaching}'" \
#                f")>"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(30), nullable=False)
#     surname = Column(String(50), nullable=False)
#     start_teaching = Column(Date, nullable=False, default='2020-01-01')
#
#
# class Student(Base):
#     __tablename__ = 'students'
#     __table_args__ = {'mysql_charset': 'utf8'}
#
#     def __repr__(self):
#         return f"<Student(" \
#                f"id='{self.id}'," \
#                f"name='{self.name}', " \
#                f"prepod_id='{self.prepod_id}'" \
#                f")>"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String(30), nullable=False)
    # prepod_id = Column(Integer, ForeignKey(f'{Prepod.__tablename__}.{Prepod.id.name}'), nullable=False)


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
