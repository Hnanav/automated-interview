from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
import os
from dotenv import load_dotenv
load_dotenv()
db = SQLAlchemy()

Base = declarative_base()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.String(50), nullable=False)
    study_group = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    participant_id = db.Column(db.String(50), nullable=False)

    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    category = db.Column(db.String(50), nullable=True)
    question_order = db.Column(db.Integer, nullable=True)
    origin = db.Column(db.String(50), nullable=False)

    chatlog_id = db.Column(db.Integer, nullable=False)


class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    question_id = db.Column(db.Integer, nullable=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    chatlog_id = db.Column(db.Integer, nullable=False)


class ChatLogLookup(db.Model):
    __tablename__ = "chat_log_lookup"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    participant_id = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )


class ChatLog(db.Model):
    __tablename__ = "chat_logs"

    id = db.Column(db.Integer, primary_key=True)
    chatlog_id = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    participant_id = db.Column(db.String(50), nullable=True)
    question_id = db.Column(db.Integer, nullable=True)
    answer_id = db.Column(db.Integer, nullable=True)
    body = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )


class AIResponse(db.Model):
    __tablename__ = "ai_responses"

    id = db.Column(db.Integer, primary_key=True)
    chatlog_id = db.Column(db.Integer, nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    model_parameters = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )


class AIModel:
    def __init__(self, model_name, chat_client, skill):
        self.role = model_name
        self.chat_client = chat_client  # Use the chat client from the Google Generative AI SDK
        self.skill = skill
        self.context = {
            "history": ""  # Initialize context with a history attribute
        }

    async def invoke_skill(self, user_input):
        """Invoke the AI model skill with the given user input."""
        # Append the user input to the context history
        self.context["history"] += f"User: {user_input}\n"

        # Create the message payload including the skill and user input
        prompt = f"{self.skill}\nUser: {user_input}"
        
        try:
            # Call the chat client and get a response
            print("du ma m")
            model = self.chat_client.GenerativeModel('gemini-1.5-flash')  # Ensure to use your specific model
            response = await model.generate_content(prompt)

            # Extract the AI response from the response object
            ai_response = response.text if response else "No response returned."
            
            # Append the AI response to the context history
            self.context["history"] += f"AI: {ai_response}\n"

            return ai_response
        
        except Exception as e:
            # Handle any exceptions that occur during the API call
            return f"Error invoking skill: {str(e)}"

# Thay đổi thông tin kết nối dưới đây
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)


def main():
    # Tạo kết nối đến cơ sở dữ liệu
    engine = create_engine(DATABASE_URI)
    # Tạo bảng nếu chưa tồn tại
    Base.metadata.create_all(engine)
    print("All tables created!")

main()
