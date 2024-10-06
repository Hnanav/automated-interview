import logging
import colorlog
from dotenv import load_dotenv
import os
import mysql.connector

def setup_logger(context):
    """Return a logger with a default ColoredFormatter."""
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(reset)s %(blue)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style="%"
    )

    logger = logging.getLogger(context)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger

logger = setup_logger(__name__)

def get_db_credentials():
    """Load database credentials from environment variables."""
    load_dotenv()  # Load environment variables from .env file

    db_credentials = {
        "DB_USERNAME": os.environ.get("DBUSERNAME"),
        "DB_PASSWORD": os.environ.get("DBPASSWORD"),
        "DB_SERVER": os.environ.get("DBSERVER"),
        "DB_DRIVER": os.environ.get("DBDRIVER"),
        "DB_DATABASE": os.environ.get("DBDATABASE"),
        "DB_SECRET_KEY": os.environ.get("DBSECRETKEY"),
    }

    # Log if any credentials are missing
    for key, value in db_credentials.items():
        if value is None:
            logger.error(f"{key} not found in environment variables")

    return db_credentials

def get_api_credentials():
    """Load API credentials from environment variables."""
    load_dotenv()  # Load environment variables from .env file
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

    if GEMINI_API_KEY is None:
        logger.error("GEMINI_API_KEY not found in environment variables")
    
    return GEMINI_API_KEY

# Get database credentials
db_creds = get_db_credentials()

try:
    conn = mysql.connector.connect(
        host=db_creds["DB_SERVER"],
        user=db_creds["DB_USERNAME"],
        password=db_creds["DB_PASSWORD"],
        database=db_creds["DB_DATABASE"]
    )
    logger.info("Connected to the database successfully")
    conn.close()
except mysql.connector.Error as err:
    logger.error(f"Database connection error: {err}")
except Exception as e:
    logger.error(f"Error: {e}")




import pymysql

connection = pymysql.connect(
    host='localhost',
    user='chatbot_user',
    password='root',
    database='promptChat'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("Database version:", version)
finally:
    connection.close()
