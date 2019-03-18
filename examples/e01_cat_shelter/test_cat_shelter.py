import pytest
from solitude.testing import sol, IContractNoCheck, TransactionError


@pytest.fixture(scope="function")
def shelter(sol):
    # deploy and return contract instance
    with sol.account(0):
        return sol.deploy("CatShelter", args=(), wrapper=IContractNoCheck)


def test_001_adopt_cat(sol, shelter):
    # adopt a cat and check you are its adopter
    CAT_ID = 3
    with sol.account(0):
        shelter.transact_sync("adopt", CAT_ID)

    assert sol.address(0) == shelter.call("adopters", 3)


def test_002_adopt_wrong_id(sol, shelter):
    # adopt a cat which does not exist and expect an error
    CAT_ID = 60
    with sol.account(0):
        with pytest.raises(TransactionError):
            # this transaction should fail
            shelter.transact_sync("adopt", CAT_ID)


def test_003_get_adopters_list(sol, shelter):
    CAT_ID = 3
    with sol.account(0):
        shelter.transact_sync("adopt", CAT_ID)
    adopters = shelter.call("getAdopters")
    assert adopters[CAT_ID] == sol.address(0)
