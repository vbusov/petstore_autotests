def test_add_pet_and_find_by_id(pet_ops):
    """
    1. Add a new pet and get its ID
    2. Find new pet by ID and check that the name is correct
    """

    new_pet = {
        'name': 'VladCat',
        'photoUrls': ['string'],
    }

    add_response = pet_ops.add_pet(new_pet)
    assert add_response.status_code == 200, 'Error creating new pet'
    assert 'id' in add_response.json(), 'No pet ID in response'
    new_pet_id = add_response.json()['id']

    find_by_id_response = pet_ops.find_pet_by_id(new_pet_id)
    assert find_by_id_response.status_code == 200, 'Error finding new pet'
    found_pet = find_by_id_response.json()
    assert found_pet['name'] == 'VladCat', 'Wrong pet found by ID'

def test_find_and_delete_existing_pet(pet_ops, prepared_pet):
    """
    1. Find prepared pet by ID
    2. Delete prepared pet by ID
    """
    prepared_pet_id = prepared_pet['id']
    find_by_id_response = pet_ops.find_pet_by_id(prepared_pet_id)
    assert find_by_id_response.status_code == 200, 'Error finding prepared pet'
    delete_pet_response = pet_ops.delete_pet(prepared_pet_id)
    assert delete_pet_response.status_code == 200, 'Error deleting pet'

def test_update_pet_and_find_by_status(pet_ops, prepared_pet):
    """
    1. Update prepared pet status
    2. Find pets by status and check for prepared pet ID
    """
    updated_status = 'test_status'
    pet_id, pet_name = (prepared_pet[field] for field in ('id', 'name'))
    update_pet_response = pet_ops.update_pet_form_data(
        pet_id, pet_name, updated_status
    )
    assert update_pet_response.status_code == 200, 'Error updating pet'
    find_pets = pet_ops.find_pets_by_status(updated_status)
    pets = find_pets.json()
    pet_ids = [pet['id'] for pet in pets]
    assert pet_id in pet_ids, 'Updated pet not found by status'
