from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, Flask
from rest_api.log.views import views


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

if __name__ == '__main__':
    app.run(debug=True)
