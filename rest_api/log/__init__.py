import logging

from logging import Logger


class MyLogger(Logger):
    """
    实现打印谁调用了方法，以及调用行数
    """

    @staticmethod
    def get_logger(name=None):
        """
        Return a logger with the specified name, creating it if necessary.
        If no name is specified, return the root logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        # 创建控制台 handler
        stream_handler = logging.StreamHandler()
        # 设置 stream handler 日志级别
        stream_handler.setLevel(logging.INFO)
        # 设置日志输出格式
        formatter_string = "[%(asctime)s] {%(className)s:%(lineno)s " \
                           "%(funcName)s:%(name)s} " \
                           "%(levelname)s - %(message)s"
        formatter = logging.Formatter(formatter_string)
        stream_handler.setFormatter(formatter)
        # 将 handler 添加到 logger 对象中
        logger.addHandler(stream_handler)
        return logger

    pass
