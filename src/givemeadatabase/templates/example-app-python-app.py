from flask import Flask
from sqlalchemy import create_engine


app = Flask(__name__)

engine = create_engine(
    "mysql+pymysql://CHANGE_WITH_YOUT_USERNAME:CHANGE_WITH_YOUR_PASSWORD@CHANGE_WITH_HOSTNAME:CHANGE_WITH_PORT/CHANAGE_WITH_YOUR_DATABASE_NAME?charset=utf8mb4",
    pool_pre_ping=True,
)


@app.route("/")
def hello_world():
    engine.connect()  # Verify database connection
    with engine.connect() as con:
        result = con.execute("SELECT NOW()")
        for row in result:
            print(row)
        return f"hello from app<br />Result of NOW() from database: {row}"

    return "hello app2"


@app.route("/test", methods=["POST"])
def test():
    return "post recieved to app"
