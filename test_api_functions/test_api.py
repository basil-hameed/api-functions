import pytest
import requests
from api_functions.functions import APIFunctions
from api_functions.mock_data import TestData

class TestAPIFunctions:

    # setup function for all test cases
    @pytest.fixture
    def setup(self):
        self.url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
        self.api_functions = APIFunctions(self.url)

    # created test case to verify status code
    def test_api_status_code(self, setup):
        assert self.api_functions.api_status_code() == 200

    
    # test case to verify fetch_data
    def test_fetch_api_data(self, setup):
        assert self.api_functions.fetch_api_data() == TestData.mock_data

    # test case to verify the header data
    def test_fetch_header(self, setup):
        headers = self.api_functions.fetch_header()
        assert headers['Server'] == 'Cowboy'

    # test case to verify the data by id
    def test_fetch_data_by_id(self, setup):
        result = self.api_functions.fetch_data_by_id(24)
        assert result == TestData.mock_data24

    # test case to verify insert data
    def test_insert_data(self, setup):
        data = {'food_name': 'Brownie', 'country': 'London'}
        assert self.api_functions.insert_data(data) == True

    # test case to delete data 
    def test_delete_data_by_id(self, setup):
        assert self.api_functions.delete_data_by_id(53) == True

