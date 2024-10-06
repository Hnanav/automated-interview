from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
# Thay đổi thông tin kết nối dưới đây
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'

Base = declarative_base()

# Định nghĩa các bảng
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    participant_id = Column(String(255), nullable=False)
    study_group = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class ChatLogLookup(Base):
    __tablename__ = 'chat_log_lookup'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    participant_id = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

def main():
    # Tạo kết nối đến cơ sở dữ liệu
    engine = create_engine(DATABASE_URI)
    # Tạo bảng nếu chưa tồn tại
    Base.metadata.create_all(engine)
    print("All tables created!")

main()
