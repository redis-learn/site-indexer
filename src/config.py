import os

db_host = os.getenv("DB_HOST")
db_host = "localhost" if db_host is None else str(db_host)
db_port = os.getenv("DB_PORT")
db_port = 6379 if db_port is None else int(db_port)
db_pwd = os.getenv("DB_PWD")
db_pwd = "" if db_pwd is None else str(db_pwd)

CFG = {
    "db_host": db_host,
    "db_port": db_port,
    "db_pwd": db_pwd
}