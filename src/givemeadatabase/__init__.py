from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

application = Flask(__name__)
application.config.update(os.environ)

import givemeadatabase.views  # noqa
