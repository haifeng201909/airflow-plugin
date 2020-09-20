from flask import Blueprint

from rest_api.service.mylog_service import MyLogTest

my_log_pb = Blueprint("my_log", __name__)


@my_log_pb.route("/", methods=['GET'])
def my_log():
    return MyLogTest.record_log()
