import requests

class APIFunctions:
    def __init__(self, url):
        self.url = url
    
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code
    
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "Error - 404"
    
    def fetch_header(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return "Error - 404"

    def fetch_data_by_id(self, id):
        if self.api_status_code() == 200:
            user_id  = str(id)
            for data in self.fetch_api_data():
                if data['id'] == user_id:
                    return (data['id'], data['food_name'], data['country'])
        return None

    def fetch_all_id_data(self):
        if self.api_status_code() == 200:
            for data in self.fetch_api_data():
                print(data['country'])

    def insert_data(self, data):
        if self.api_status_code() == 200:
            response = requests.post(self.url, json=data)
            return response.status_code == 201
        return False

    def delete_data_by_id(self, id):
        if self.api_status_code() == 200:
            delete_url = f"{self.url}/{id}"
            response = requests.delete(delete_url)
            return response.status_code == 200
        return False



url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
data = {'food_name': 'Brownie', 'country': 'India'}
myapi = APIFunctions(url)
# print(myapi.api_status_code())
# print(myapi.fetch_api_data())
# print(myapi.fetch_header())
# print(myapi.fetch_data_by_id(24))
# print(myapi.fetch_all_id_data())
# print(myapi.insert_data(data))
# print(myapi.delete_data_by_id(52))
