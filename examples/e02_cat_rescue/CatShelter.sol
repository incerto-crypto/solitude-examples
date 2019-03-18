pragma solidity ^0.5.2;

contract CatShelter
{
    address owner;
    address[] public adopters;

    event Rescued(uint256 catId);

    constructor() public
    {
        owner = msg.sender;
    }

    function adopt(uint256 catId) public
    {
        require(catId < adopters.length);
        require(
            adopters[catId] == address(0),
            "Cat has already been adopted");
        adopters[catId] = msg.sender;
    }

    function rescue() public
    {
        require(msg.sender == owner);
        adopters.push(address(0));
        emit Rescued(adopters.length - 1);
    }
}
