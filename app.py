from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient

app = Flask(__name__)

# db info
mongo_uri = "mongodb://127.0.0.1:27017"
client = MongoClient(mongo_uri)
db = client['steam']        # database
dofitos = db['dofitos']     # collection

# scheduler api calls
scheduler = BackgroundScheduler()
scheduler.start()


def update_database_data():
    dofitos.insert({"nombre": "insertado desde scheduler"})
    print("Hola")


scheduler.add_job(update_database_data, "interval", seconds=5)


@app.route('/')
def hello_world():
    return "home"


@app.route('/insert')
def insert_dummy():
    res = dofitos.insert({"nombre": "insertado desde flask"})
    return "ok"


if __name__ == '__main__':
    app.run()
