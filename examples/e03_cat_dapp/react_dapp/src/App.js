import React, { Component } from 'react';
import { Card, Container } from 'semantic-ui-react'      
import Web3 from 'web3';
import './App.css';

class App extends Component {

  constructor() {
    super()
    this.WEB3_HTTP_PROVIDER = 'http://localhost:8545';
    this.CAT_SHELTER_WEBSITE = 'http://localhost:8546';
    this.CONTRACT_ENDPOINT = '/api/v1/contract';
    this.NULL_ADDRESS = '0x0000000000000000000000000000000000000000';
    this.GAS = '2655150';
    this.GAS_PRICE = '700000000';
    this.state = {
      adoptersArray: null,
      address: null,
      abi: null,
      web3: null,
      contract: null,
    }
    this.makeAdoption = this.makeAdoption.bind(this)
    this.getAdopters = this.getAdopters.bind(this)
  }

  componentWillMount() {
    this.initWeb3().then(provider =>
      this.setState({ web3: provider })).then(() => {
        return fetch(`${this.CAT_SHELTER_WEBSITE}${this.CONTRACT_ENDPOINT}`);
      }
      ).then(response => response.json())
      .then(contractInfo => {
        this.setState(contractInfo)
        return this.initContract()
      }).then(contractCatShelter => {
        this.setState(contractCatShelter);

      })
  }

  render() {
    this.getAdopters();
    if (this.state.adoptersArray == null) {
      return false
    }
    return (
      <div className="App page">
        <h1> Cat-Shelter React Dapp </h1>
        <Container className="shelter_container">
          <div className="ui two column stackable center aligned page grid">
            {
              this.state.adoptersArray.map((address, index) => (
                <div key={index}>
                  <Card>
                    <Card.Content
                      header={`Cat#${index + 1}`}
                      meta={address === this.NULL_ADDRESS ? `Owner: ORPHANED` :
                        `Owner: ${address.substring(0, 4)}...${address.substring(address.length - 4)}`}
                    />
                    <Card.Content extra>
                      {address === this.NULL_ADDRESS ?
                        <button onClick={() => this.makeAdoption(index)}>ADOPT</button>
                        :
                        <p>Adopted</p>
                      }
                    </Card.Content>
                  </Card>
                </div>
              ))
            }
          </div>
        </Container>
      </div>
    );
  }

  async initWeb3() {
    let web3Provider = null;
    if (window.ethereum) {
      web3Provider = window.ethereum;
      try {
        await window.ethereum.enable();
      } catch (error) {
        console.error("User denied account access")
      }
    }
    else if (window.web3) {
      web3Provider = window.web3.currentProvider;
    }
    else {
      web3Provider = new Web3.providers.HttpProvider(this.WEB3_HTTP_PROVIDER);
    }

    return new Web3(web3Provider);
  }

  initContract() {
    let contractCatShelter = new this.state.web3.eth.Contract(this.state.abi, this.state.address, {});
    return { contract: contractCatShelter }
  }

  getAdopters() {
    if (this.state.contract == null) {
      return false;
    }
    return this.state.contract.methods.getAdopters().call().then(
      adoptersArray => {
        this.setState({ adoptersArray: adoptersArray })
      })
  }

  makeAdoption(catId) {
    this.state.web3.eth.getAccounts().then(accounts => {
      var txnObject = {
        from: accounts[0],
        gas: this.GAS,
        gasPrice: this.GAS_PRICE
      }
      this.state.contract.methods.adopt(catId).send(txnObject).then(data => {
        this.forceUpdate()
      });
    })
  }
}

export default App;
