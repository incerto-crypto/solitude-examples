# Cat Shelter example

## Description

Adopt your cat on the blockchain and it will be yours for ever.

There are only 16 cats in this shelter: get yours before they're all gone!

`CatShelter` contract functions:
- `adopt(uint256 catId)`: adopt a cat, catId must be a number between 0 and 15, a cat cannot be adopted twice
- `getAdopters()`: get a list containing the adopter's address for each cat.


## Instructions

Compile the contracts by running

```bash
solitude compile
```

Then run the tests with
```bash
pytest -v test_cat_shelter.py
```
