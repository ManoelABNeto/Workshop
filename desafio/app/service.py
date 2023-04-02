from rest_framework.exceptions import NotFound
import requests
import os


class WeatherModel:
    def __init__(self, main: str, description: str):
        self.main = main
        self.description = description
    

class WeatherApi:
    API_WEATHER_KEY = os.getenv('API_WEATHER_KEY')
    API_WEATHER_URL = os.getenv('API_WEATHER_URL')
    
    @staticmethod
    def obtem_clima_por_cidade(cidade: str) -> WeatherModel:
        
        url = f'{WeatherApi.API_WEATHER_URL}weather?q={cidade}&appid={WeatherApi.API_WEATHER_KEY}'
        response = requests.get(url)

        if response.status_code != 200:
            raise NotFound('Cidade não foi encontrada na WEATHER_API!')
        
        response = response.json()
        return WeatherModel(main = response['weather'][0]['main'], description = response['weather'][0]['description'])
