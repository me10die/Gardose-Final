from app import app
from final_database.mysql import MYSQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'rest-api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)