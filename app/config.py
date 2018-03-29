import pymysql
# MYSQL
SQLALCHEMY_BINDS = {
    'mysql':'mysql+pymssql://root:root@127.0.0.1:3306/egp?charset=utf8'
}
SQLALCHEMY_TRACK_MODIFICATIONS = True