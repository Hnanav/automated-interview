
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, DateTime
load_dotenv()
# Thay đổi thông tin kết nối dưới đây
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'
engine = create_engine(DATABASE_URI)
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

class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    participant_id = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)
    question_id = Column(Integer, nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.timezone.utc)
    chatlog_id = Column(Integer, nullable=False)


class ChatLog(Base):
    __tablename__ = 'chat_logs'

    chatlog_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    participant_id = Column(String(255), nullable=False)
    question_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=True)
    body = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.timezone.utc)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    participant_id = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.timezone.utc)
    category = Column(String(50), nullable=False)  # Giả sử category là một chuỗi
    question_order = Column(Integer, nullable=False)  # Thứ tự câu hỏi
    origin = Column(String(50), nullable=False)  # Nguồn gốc câu hỏi
    chatlog_id = Column(Integer)  # ID của chat log

class AIResponse(Base):
    __tablename__ = 'ai_responses'
    
    id = Column(Integer, primary_key=True)
    chatlog_id = Column(Integer, nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    model_parameters = Column(String(255), nullable=False)  # Use VARCHAR(255) with a length limit

    created_at = Column(DateTime, default=datetime.timezone.utc)

def main():
    # Tạo kết nối đến cơ sở dữ liệu
    engine = create_engine(DATABASE_URI)
    # Tạo bảng nếu chưa tồn tại
    Base.metadata.create_all(engine)
    print("All tables created!")

main()
