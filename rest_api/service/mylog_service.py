"""
测试自定义 logger
"""
import logging

from rest_api.log import MyLogger


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
