import logging


class NativeLogService:

    @staticmethod
    def native_log():
        # 获取一个 logger 对象
        logger = logging.getLogger("native_log")

        # 需要 logger 以及 file_handler 同时开启 DEBUG 级别
        # 否则 DEBUG 日志不会打印文件
        logger.setLevel(logging.DEBUG)

        # 创建文件 handler
        file_handler = logging.FileHandler("native_log.log")
        # 创建控制台 handler
        stream_handler = logging.StreamHandler()

        # 设置文件 handler 日志等级
        file_handler.setLevel(logging.DEBUG)
        #
        stream_handler.setLevel(logging.INFO)

        # 设置日志输出格式
        formatter = logging.Formatter(
            "[%(asctime)s] {%(filename)s:%(lineno)s %(funcName)s:%(name)s} %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 将 handler 添加到 logger 对象中
        logger.addHandler(file_handler)
        # logger.addHandler(stream_handler)

        logger.info(__name__)
        logger.error(__name__)
        logger.debug(__name__)
        return __name__
