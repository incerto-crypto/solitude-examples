import time
import binascii
from solitude import read_config_file, Factory


def print_txinfo(txinfo):
    txhash = "0x" + binascii.hexlify(txinfo.txhash).decode()
    print("TX FROM {user}".format(
        user=txinfo.txargs["from"]
    ))
    print("   TO {contract}@{address}".format(
        contract=txinfo.contractname,
        address=txinfo.address
    ))
    print("   FUNCTION {name}{args}".format(
        name=txinfo.function,
        args=repr(txinfo.fnargs)))
    print("   TXHASH %s" % txhash)
    print("")


def main():
    factory = Factory(read_config_file("solitude.yaml"))
    server = factory.create_server()
    server.start()
    try:
        client = factory.create_client()
        client.update_contracts(factory.get_objectlist())
        owner = client.address(0)
        george = client.address(1)

        with client.account(owner):
            token = client.deploy("MyToken", args=("Token", "TKN", 0))
            txinfo = token.transact_sync("mint", owner, 1000)
            print_txinfo(txinfo)
            txinfo = token.transact_sync("transfer", george, 100)
            print_txinfo(txinfo)
        print("Ctrl-C to quit")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("")
    finally:
        server.stop()


if __name__ == "__main__":
    main()
