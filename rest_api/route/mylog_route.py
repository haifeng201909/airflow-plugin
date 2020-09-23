from flask import Blueprint

from rest_api.service.mylog_service import MyLogTest, CustomAdapterTest

my_log_pb = Blueprint("my_log", __name__)


@my_log_pb.route("/", methods=['GET'])
def my_log():
    return MyLogTest.record_log()


@my_log_pb.route("/custom", methods=['GET'])
def custom_log():
    return CustomAdapterTest.record_log()
