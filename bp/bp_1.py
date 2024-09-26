from flask import Blueprint, jsonify
from models.Mission import Mission

bp_1_bp = Blueprint("admin", __name__, url_prefix="/api/mission")

@bp_1_bp.route("/", methods=["GET"])
def get_all_missions():
    missions = Mission.query.all()
    return jsonify([mission.__dict__ for mission in missions if '_sa_instance_state' not in mission.__dict__]), 200


