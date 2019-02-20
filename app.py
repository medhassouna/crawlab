from celery import Celery
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# TODO: 用配置文件启动 http://www.pythondoc.com/flask/config.html
app = Flask(__name__)
app.config['DEBUG'] = True

# celery_app
celery_app = Celery(__name__)
celery_app.config_from_object('config.celery')

# init flask api instance
api = Api(app)

# cors support
CORS(app, supports_credentials=True)

# reference api routes
import routes.nodes
import routes.spiders
import routes.deploys
import routes.tasks
import routes.files

# start flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
