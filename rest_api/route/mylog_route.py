from flask import Blueprint

my_log_pb = Blueprint("my_log", __name__)


@my_log_pb("/", methods=['GET'])
def my_log():
    pass
