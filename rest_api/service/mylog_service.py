"""
测试自定义 logger
"""
import logging

from rest_api.log import MyLogger
from rest_api.log.my_log import CustomAdapter


class MyLogTest:
    """
    测试自定义日志类的使用
    """

    @staticmethod
    def record_log():
        logger = MyLogger.get_logger("my_log")
        extra_msg = {"className": "class name"}
        logger.info("MyLogTest", extra=extra_msg)
        return "MyLogTest"


class CustomAdapterTest:
    """
    测试 CustomAdapter
    """
    @staticmethod
    def record_log():
        logger = logging.getLogger(__name__)
        adapter = CustomAdapter(logger, {'conn_id': 'my_conn_id'})
        adapter.error("==========")
        return "CustomAdapter"

