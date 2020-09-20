from flask import Blueprint

from rest_api.service.native_log_service import NativeLogService

native_log_bp = Blueprint("native_log", __name__)


@native_log_bp.route("/", methods=['GET'])
def native_log():
    return NativeLogService.native_log()
