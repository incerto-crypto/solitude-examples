# Cat Rescue example

## Description

This shelter starts empty. Its owner occasionally rescues cats and brings them to the shelter.

But these new entries won't last long. One greedy adopter is watching for new cats and adopting them as soon as they come.


`CatShelter` contract functions:
- `adopt(uint256 catId)`: adopt a cat, catId must be a number between 0 and 15, a cat cannot be adopted twice
- `rescue()`: add a new cat to the shelter, only the shelter owner can do this

Note: the shelter owner is the address which deploys the shelter contract.


## Instructions

Compile the contracts by running

```bash
solitude install  # install any needed external tools
solitude compile
```

Run the shelter simulation with
```bash
python cat_rescue.py
```
