import time
import threading
from solitude import read_config_file, Factory
from solitude.client import IContractNoCheck, ETHClient


def deploy(client: ETHClient):
    owner = client.address(0)
    with client.account(owner):
        shop = client.deploy("CatShelter", args=(), wrapper=IContractNoCheck)
    return shop.address


def rescue_cats(client: ETHClient, shop_address):
    owner = client.address(0)
    shop = client.use("CatShelter", shop_address, wrapper=IContractNoCheck)
    with client.account(owner):
        for _ in range(3):
            time.sleep(2)
            print("Owner (%s) rescued a new cat" % owner)
            shop.transact_sync("rescue")


def adopt_cats(client: ETHClient, shop_address):
    adopter = client.address(1)
    shop = client.use("CatShelter", shop_address, wrapper=IContractNoCheck)

    flt = client.add_filter([shop], ["Rescued"])
    def watch_and_adopt():
        for log in client.iter_filters([flt]):
            catId = log.data.args["catId"]
            with client.account(adopter):
                print("User (%s) is adopting Cat #%d" % (adopter, catId))
                shop.transact_sync("adopt", catId)

    thread = threading.Thread(target=watch_and_adopt)
    thread.start()
    time.sleep(10)
    client.remove_filter(flt)
    thread.join()


def main():
    factory = Factory(read_config_file("solitude.yaml"))
    server = factory.create_server()
    server.start()
    endpoint = server.endpoint
    try:
        client1 = factory.create_client(endpoint=server.endpoint)
        shop_address = deploy(client1)
        thread_rescue = threading.Thread(target=rescue_cats, args=(client1, shop_address))
        thread_rescue.start()

        client2 = factory.create_client(endpoint=server.endpoint)
        thread_adopt = threading.Thread(target=adopt_cats, args=(client2, shop_address))
        thread_adopt.start()

        thread_rescue.join()
        thread_adopt.join()
    finally:
        server.stop()


if __name__ == "__main__":
    main()
