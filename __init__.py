from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, Flask
from rest_api.log.views import views
from rest_api.route.log_route import log
from rest_api.route.mylog_route import my_log_pb
from rest_api.route.native_log_route import native_log_bp


class AirflowPlugin(AirflowPlugin):
    name = "airflow-plugin"
    operators = []
    # Leave in for explicitness
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []


# 创建Blueprint实例
# Blueprint实例创建之后我们就可以通过@Blueprint实例名.route('/')语法为我们的模块创建路由
airflow_bp = Blueprint(
    'airflow_bp',
    __name__
)


app = Flask(__name__)

# 注册我们在views.py模块中创建的蓝图实例views, 并将他的URL前缀设置为`/views`
app.register_blueprint(views, url_prefix='/views')

app.register_blueprint(log, url_prefix='/')

app.register_blueprint(native_log_bp, url_prefix='/native_log')

app.register_blueprint(my_log_pb, url_prefix='/my_log')

if __name__ == '__main__':
    app.run(debug=True)
