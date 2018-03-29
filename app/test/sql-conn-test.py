mysql_db_username = 'root'
mysql_db_password = 'root'
mysql_db_name = 'egp'
mysql_db_host = 'localhost'
mysql_db_port = 3306
mysql_db_conn_pool_conf = 'charset=utf8'
SQLALCHEMY_BINDS = {
    'mysql': "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?{DB_CONN_POOL_CONF}".format(
                                                                              DB_USER=mysql_db_username,
                                                                              DB_PASS=mysql_db_password,
                                                                              DB_ADDR=mysql_db_host,
                                                                              DB_PORT=mysql_db_port,
                                                                              DB_NAME=mysql_db_name,
                                                                              DB_CONN_POOL_CONF=mysql_db_conn_pool_conf)
}
print SQLALCHEMY_BINDS['mysql']