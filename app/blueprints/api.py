from flask import Blueprint

api_bp = Blueprint('api', __name__ )

@api_bp.route('/example')
def example():
    return {"message":"This is an example"}