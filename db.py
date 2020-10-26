from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# create table `user`(`id` VARCHAR(20), `name` VARCHAR(20), primary key (`id`))engine=InnoDB default charset=utf8;
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

connection='mysql+pymysql://root@127.0.0.1/test'
engine = create_engine(connection)
DBSession = sessionmaker(bind=engine)
new_user = User(id='5', name='Bob')

# ADD
print('ADD')
session = DBSession()
session.add(new_user)
session.commit()
session.close()

# GET
print('GET')
session = DBSession()
ret = session.query(User).first()
session.close()
print(ret.id, ret.name)

# DELETE
print('DELETE')
session = DBSession()
session.delete(ret)
session.commit()
session.close()


