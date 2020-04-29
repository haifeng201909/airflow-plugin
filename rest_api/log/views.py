from flask import Blueprint


# 创建Blueprint实例
views = Blueprint('views', __name__)


# Blueprint实例创建之后我们就可以通过@Blueprint实例名.route('/')语法为我们的模块创建路由
@views.route('/')
def index():
    return 'This is views index'
