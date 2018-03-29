from app import db,app
from app.model.Article import Article
from app.model.User import User
import time
art1 = Article(title="tt", author='admin', content='dadadad', create_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
user1 = User(account='5555',password='adas', create_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,comment='ada')
db.session.add(art1)
db.session.add(user1)
db.session.commit()
