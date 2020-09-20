import logging

from flask import Blueprint

from rest_api.service.log_service import LogService

log = Blueprint("log", __name__)


@log.route("/", methods=['GET'])
def log_test():
    logger = logging.getLogger("log")
    logger.error("function log_test called")
    return LogService.log_test()
