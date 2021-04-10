from flask import Flask

app = Flask(__name__)


stores = [
    {
        "name": "MY store"
        "Items": [
            {
                "name": "MY item"
                "price": 20
            }
        ]
    }
]

@app.route("/store", methods=["POST"])
def create_stores():
    pass

@app.route("/store/<string:name>")
def get_store(name):
    pass


@app.route("/store")
def get_stores():
    pass


@app.route("/store/<string:name>/item", methods=["POST"])
def create_items_stores(name):
    pass


@app.route("/store/<string:name>/item")
def get_items_stores(name):
    pass


app.run(port=5000)