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
        return logging.getLogger(name)

    pass
