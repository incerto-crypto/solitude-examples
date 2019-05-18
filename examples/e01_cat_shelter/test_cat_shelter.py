import pytest
from solitude.testing import sol
from solitude.errors import TransactionError


@pytest.fixture(scope="function")
def account0(sol):
    return sol.address(0)


@pytest.fixture(scope="function")
def shelter(sol, account0):
    # deploy and return contract instance
    with sol.account(account0):
        return sol.deploy("CatShelter", args=())


def test_001_adopt_cat(sol, shelter, account0):
    # adopt a cat and check you are its adopter
    CAT_ID = 3
    with sol.account(account0):
        shelter.transact_sync("adopt", CAT_ID)

    assert sol.address(0) == shelter.call("adopters", 3)


def test_002_adopt_wrong_id(sol, shelter, account0):
    # adopt a cat which does not exist and expect an error
    CAT_ID = 60
    with sol.account(account0):
        with pytest.raises(TransactionError):
            # this transaction should fail
            shelter.transact_sync("adopt", CAT_ID)


def test_003_get_adopters_list(sol, shelter, account0):
    CAT_ID = 3
    with sol.account(account0):
        shelter.transact_sync("adopt", CAT_ID)
    adopters = shelter.call("getAdopters")
    assert adopters[CAT_ID] == account0
