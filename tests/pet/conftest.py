import pytest

from petstore.config import PETSTORE_URL, API_KEY
from petstore.pet import PetOperations


@pytest.fixture
def pet_ops():
    """Pet operations fixture"""
    return PetOperations(PETSTORE_URL, API_KEY)

@pytest.fixture
def prepared_pet():
    """Prepared pet fixture for tests"""
    pet_ops = PetOperations(PETSTORE_URL, API_KEY)
    new_pet_body = {
        'name': 'test_pet',
        'photoUrls': ['string'],
    }
    try:
        new_pet = pet_ops.add_pet(new_pet_body)
        new_pet_id = new_pet.json()['id']
    except Exception:
        assert False, 'Error in preparing pet fixture'
    yield new_pet.json()
    pet_ops.delete_pet(new_pet_id)

