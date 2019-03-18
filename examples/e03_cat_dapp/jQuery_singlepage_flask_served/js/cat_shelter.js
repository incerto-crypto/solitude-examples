CatShelterApp = {
  CONTRACT_NAME: 'catShelter',
  NULL_ADDRESS: '0x0000000000000000000000000000000000000000',
  web3Provider: null,
  contracts: {},
  
  initWeb3: async function () {
    if (window.ethereum) {
      CatShelterApp.web3Provider = window.ethereum;
      try {
        await window.ethereum.enable();
      } catch (error) {
        console.error("User denied account access")
      }
    }
    else if (window.web3) {
      CatShelterApp.web3Provider = window.web3.currentProvider;
    }
    else {
      CatShelterApp.web3Provider = new Web3.providers.HttpProvider('http://localhost:8545');
    }
    web3 = new Web3(CatShelterApp.web3Provider);
    return CatShelterApp.initContract();
  },

  initContract: function () {
    address = $("#address").text();
    abi = $.parseJSON($("#abi").html());
    contractCatShelter = new web3.eth.Contract(abi, address, {});
    CatShelterApp.contracts[CatShelterApp.CONTRACT_NAME] = contractCatShelter;
    contractCatShelter.methods.getAdopters().call().then(function (data) {
      $.each(data, function (i, item) {
        if (item == CatShelterApp.NULL_ADDRESS) {
          $("#catlist").append('<li><div><p>CatId:' + i +
            '</p><button onclick="CatShelterApp.makeAdoption(' + i +
            ')">Adopt</button></div></li>');
        }
        else {
          $("#catlist").append('<li><div><p>CatId:' + i +
            '</p><p>&nbsp&nbspOwner: ' + item +
            '</p></div></li>');
        }
      });
    })
  },

  makeAdoption: function (catId) {
    web3.eth.getAccounts().then(function (accounts) {
      var txnObject = {
        from: accounts[0],
        gas: '2655150',
        gasPrice: '700000000'
      }
      console.log(accounts);
      contractCatShelter = CatShelterApp.contracts[CatShelterApp.CONTRACT_NAME]
      contractCatShelter.methods.adopt(catId).send(txnObject).then(function (data) {
        console.log('Adopted')
        console.log(data);
        location.reload();
      });
    });
  },

};

$(function () {
  $(window).load(function () {
    CatShelterApp.initWeb3();
  });
});

