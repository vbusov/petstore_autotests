import requests


class PetOperations:
    """Everything about your Pets"""
    
    def __init__(self, petstore_url, api_key):
        self.url = f'{petstore_url}/pet'
        self.api_key = api_key

    def find_pet_by_id(self, pet_id):
        endpoint = f'{self.url}/{pet_id}'
        return requests.get(endpoint)
    
    def find_pets_by_status(self, status):
        endpoint = f'{self.url}/findByStatus'
        params = {'status': status}
        return requests.get(endpoint, params=params)
    
    def add_pet(self, pet_object):
        endpoint = f'{self.url}'
        return requests.post(endpoint, json=pet_object)
    
    def update_pet_object(self, pet_object):
        endpoint = f'{self.url}'
        return requests.put(endpoint, json=pet_object)
    
    def update_pet_form_data(self, pet_id, name, status):
        endpoint = f'{self.url}/{pet_id}'
        data = {
            'name': name,
            'status': status
        }
        return requests.post(endpoint, data=data)
    
    def delete_pet(self, pet_id):
        endpoint = f'{self.url}/{pet_id}'
        headers = {'api_key': self.api_key}
        return requests.delete(endpoint, headers=headers)
