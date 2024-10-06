# Set Up step

### Tạo database mysql

```
pip install requirements.txt
```
Trong command line nhập
```
mysql -u root -p
```
Nếu không đăng nhập thành công thì:
1. Khởi động MySQL mà không cần xác thực:
```
sudo mysqld_safe --skip-grant-tables &
```
2. Đăng nhập vào MySQL:
```
mysql -u root -p
```
3. Cập nhật mật khẩu root:
```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
```

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

```
FLUSH PRIVILEGES;
```

```
CREATE DATABASE promptChat;
```

```
exit
```

Sau đó cập nhật file .env cho đúng password, DB_DATABASE đã nhập ở command line.

### Tạo table

```
python src/create_databases.py 
```
Chạy thử
```
python src/main.py
```