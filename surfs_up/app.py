# Import Flask
from flask import Flask

# # create a new Flask instance called app
app = Flask(__name__)

# # Create Flask Routes
@app.route('/')
def hello_world():
    return 'Testing to Make Sure Flask is Working in the surfs_up folder'


# set FLASK_APP=app.py <-Ran in terminal

# flask run <-Ran in terminal
