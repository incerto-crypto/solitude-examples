import time
import threading
import json
from flask import Flask, Response, render_template, send_from_directory
from solitude import read_config_file, Factory
from solitude.client import ETHClient

app = Flask(__name__)
HTTP_SERVER_PORT = 8546
ADOPTER_CAPACITY = 2


def deploy(client: ETHClient):
    owner = client.address(0)
    with client.account(owner):
        shelter = client.deploy("CatShelter", args=())
    return shelter


@app.route('/api/v1/contract', methods=['GET'])
def get_main_contract():
    return Response(json.dumps({"abi" : app.shelter.abi, "address": app.shelter.address}), mimetype='application/json')


@app.route('/')
def render_static(page_name=None):
    return render_template('index.html', data={"abi" : json.dumps(app.shelter.abi), "address": app.shelter.address})


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def rescue_cats(client: ETHClient, shelter_address):
    owner = client.address(0)
    shelter = client.use("CatShelter", shelter_address)
    with client.account(owner):
        for _ in range(10):
            time.sleep(2)
            print("Owner (%s) rescued a new cat" % owner)
            shelter.transact_sync("rescue")


def main():
    factory = Factory(read_config_file("solitude.yaml"))
    server = factory.create_server()
    server.start()
    endpoint = server.endpoint
    try:
        client1 = factory.create_client(endpoint=server.endpoint)
        client1.update_contracts(factory.get_objectlist())
        app.shelter = deploy(client1)
        shelter_address = app.shelter.address
        thread_rescue = threading.Thread(target=rescue_cats, args=(client1, shelter_address))
        thread_rescue.start()

        app.run(port=HTTP_SERVER_PORT)
    except KeyboardInterrupt:
        thread_rescue.join()
        server.stop()
        print("Quit")


if __name__ == "__main__":
    main()
