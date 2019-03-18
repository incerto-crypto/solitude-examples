pragma solidity ^0.5.2;

contract CatShelter
{
    address[16] public adopters;

    constructor() public
    {
    }

    function adopt(uint256 catId) public
    {
        require(catId < adopters.length);
        require(
            adopters[catId] == address(0),
            "Cat has already been adopted");
        adopters[catId] = msg.sender;
    }

    function getAdopters() public view returns (address[16] memory)
    {
        return adopters;
    }
}
