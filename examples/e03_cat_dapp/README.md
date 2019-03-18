# Cat Shelter Dapp

## Description

The Cat Shelter is running a distributed app on the blockchain. 
The shelter starts empty. Its owner occasionally rescues cats and brings them to the shelter.
To make the adoption journey easier, the Cat Sheleter webiste allows to adopt orphaned cats and tracks the ownership through an Ethereum blockchain.

## Contract

`CatShelter` contract functions:
- `getAdopters()`: get the list of the cats's owners addresses. The index in the list is the cat identifier (catId). Orphaned cats have the 0x00 address as owner
- `adopt(uint256 catId)`: adopt a cat, catId must be a number between 0 and 15, a cat cannot be adopted twice
- `rescue()`: add a new cat to the shelter, only the shelter owner can do this

Note: the shelter owner is the address which deploys the shelter contract.

## Examples

In this examples there are two flavours of the cat shelter distributed app:

 - JQuery single page served by a Flask App
 - React App that interacts with a Flask App


## Jquery - Flask

The file `cat_dapp.py` contains a [Flask](http://flask.pocoo.org/) simple webapp. 
It creates an ethereum node-server and a client able to communicate with the ethereum node on (http://localhost:8545). 
The Flask app deploys the CatShelter contract on the node and gets the contract instance address. Finally it exposes to a webpage on the (http://localhost:8546) with the contract address and the abi. 
The webpage communicates direclty with contract on the ethereum-node through a JS script in the web page.
For each orphaned cat it also shows a button that allows to trigger a transaction to the node-server for adopting it. 


## Instructions

Install the missing Solidity dev tools
```bash
solitude install
```
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

Visit the CatShelter WebSite

http://localhost:8546


_Note:_ if you use Metamask or Mist, please connect to the Ethereum node-server (http://localhost:8545)


## React Dapp

The folder `react_dapp` contains a simple React app  for the frontend that interacts with a small Flask webapp for the backend. 
The Flask webapp starts the ethereum node and deploys the Cat Shelter contract.
It exposes an API ('/api/v1/contract') to fecth the deployed contract info: address and abi.
The Cat Shelter Web page shows the cats managed by the Shelter. Orphaned cats can be adopted by clicking the Adopt button.

## Instructions

You can run this demo using npm:

Install all the Node and Solitude dependecies and compile the Cat Shelter contract.

```bash
npm run primer
```

Run the Flask app for deploying the contract and making available the contract address and abi.

```bash
npm run dev
```

This commands deploys the contract first, starts the Flask server and after a few second runs the React test app.

_Note:_ if you use Metamask or Mist, please connect to the Ethereum node-server (http://localhost:8545)