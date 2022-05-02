from givemeadatabase import application as app
from flask import render_template
import subprocess
import json


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def create_database():
    msg = {}
    no_errors = True
    db_connection = False
    try:
        cmd = subprocess.run(
            app.config["CREATE_DATABASE_SCRIPT_PATH"],
            shell=True,
            capture_output=True,  # noqa: E401
        )
        if "ERROR 1007" in cmd.stderr.decode("utf-8"):
            msg["text"] = "ERROR 1007, database already exists"
        elif "ERROR" in cmd.stderr.decode("utf-8"):
            msg["text"] = cmd.stderr.decode("utf-8")
        else:
            msg["text"] = cmd.stdout.decode("utf-8")
    except Exception as e:  # noqa: F841
        msg["text"] = f"Unknown error creating database: {e}"

    if no_errors:
        try:
            db_connection = json.loads(msg["text"])
        except json.decoder.JSONDecodeError as e:
            print(f"could not decode {e}. cmd: {cmd.stderr.decode('utf-8')}")

    return render_template("index.html", msg=msg, db_connection=db_connection)
