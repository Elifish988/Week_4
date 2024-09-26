from flask import Flask
from bp.bp_1 import bp_1_bp
from db import connection_pool



app = Flask(__name__)


# יצירת הדאטה בייס
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///postgres:admin@localhost:5432/missions_wwii'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# חיבורי בלו פרינט
app.register_blueprint(bp_1_bp)




# Closing the connection pool when app shuts down
@app.teardown_appcontext
def close_pool(exception=None):
    if connection_pool:
        connection_pool.closeall()


if __name__ == "__main__":
    app.run(debug=True)
