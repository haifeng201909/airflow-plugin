from logging import Logger


class LogService(Logger):

    @staticmethod
    def log_test():
        print("LogService --->>> log_test called")
        return "log"
