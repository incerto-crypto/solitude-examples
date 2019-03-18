# Cat React Shelter Dapp

## Description

The Cat Shelter is running a distributed app on the blockchain. 
The shelter starts empty. Its owner occasionally rescues cats and brings them to the shelter.
To make the adoption journey easier, the Cat Sheleter webiste allows to adopt orphaned cats and check who is their current owner.

`CatShelter` contract functions:
- `getAdopters()`: get the list of the cats's owners addresses. The index in the list is the cat identifier (catId). Orphaned cats have the 0x00 address as owner
- `adopt(uint256 catId)`: adopt a cat, catId must be a number between 0 and 15, a cat cannot be adopted twice
- `rescue()`: add a new cat to the shelter, only the shelter owner can do this

Note: the shelter owner is the address which deploys the shelter contract.

The file `cat_dapp.py` contains a [Flask](http://flask.pocoo.org/) simple webapp. 
Using the options in the `solitude.yaml` it creates an ethereum node-server and a client able to communicate with the node-sever on (http://localhost:8545). 
The client deploys the CatShelter contract on the node-server and gets the contract instance address. The webapp exposes to a webpage on the (http://localhost:8546) the contract address and abi. 
The webpage communicates with the node-server through a JS script and shows the list of cats and their adopters.
For each orphaned cat it also shows a button that allows to trigger a transaction to the node-server for adopting it. 


## Instructions

Compile the contracts by running
```bash
solitude compile
```
Install the webapp missing requirements
```bash
pip install -r requirements.txt
```

Run the Cat Shelter Dapp with
```bash
python cat_dapp.py
```
The Cat Shelter Dapp implemented in C

Visit the CatShelter WebSite

http://localhost:8546


_Note:_ if you use Metamask or Mist, please connect to the Ethereum node-server (http://localhost:8545)
