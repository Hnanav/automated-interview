import pymysql
from utils import get_db_credentials

def check_mysql_connection():
    db_credentials = get_db_credentials()
    DB_USERNAME = db_credentials["DB_USERNAME"]
    DB_PASSWORD = db_credentials["DB_PASSWORD"]
    DB_SERVER = db_credentials["DB_SERVER"]
    DB_DATABASE = db_credentials["DB_DATABASE"]
    
    print(DB_USERNAME)
    print(DB_PASSWORD)
    print(DB_USERNAME)
    print(DB_PASSWORD)
    try:
        connection = pymysql.connect(
            host='localhost',        # Địa chỉ của MySQL server (có thể thay bằng '127.0.0.1')
            user=DB_USERNAME,             # Tên người dùng MySQL
            password=DB_PASSWORD,       # Mật khẩu của MySQL
            database=DB_DATABASE    # Tên cơ sở dữ liệu
        )
        print("Kết nối thành công!")
        connection.close()
    except pymysql.MySQLError as e:
        print("Kết nối thất bại:", e)

# Gọi hàm để kiểm tra kết nối
check_mysql_connection()