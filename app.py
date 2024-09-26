from flask import Flask
import logging
from db import connection_pool
# חיבורי בלו פרינט
# from postgres_proj.bp.admin import admin_bp
# from postgres_proj.bp.worker import worker_bp


app = Flask(__name__)

# חיבורי בלו פרינט
# app.register_blueprint(admin_bp, url_prefix="/admin")
# app.register_blueprint(worker_bp, url_prefix="/worker")


# Closing the connection pool when app shuts down
@app.teardown_appcontext
def close_pool(exception=None):
    if connection_pool:
        connection_pool.closeall()


if __name__ == "__main__":
    app.run(debug=True)
