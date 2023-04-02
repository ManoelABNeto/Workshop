# API Localização/Clima - Django REST Framework
Este projeto é baseado em Django RESTful API para gerenciamento de uma base de dados de localização e clima. Essa API permite ao usuário a utilização das operações do CRUD (create, read, update, delete) para as entidades Estado, Cidade e Clima via requisições HTTP. 

## Requisitos
* Python 3.11
* Django 4.1
* Django REST framework 3.14
* PostgreSQL Database
* Requests 2.28
  

## Instalação
1\. Clonar o repositório do projeto:
```
git clone https://github.com/ManoelABNeto/workshop/tree/desafio
```
2\. Criar um ambiente virtual.

3\. Instalar as dependências:
```
pip install -r requirements.txt
```
4\. Criar um arquivo .env na raiz do projeto (desafio) com as seguintes variáveis: 
```
DB_ENGINE='django.db.backends.postgresql_psycopg2'
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT

API_WEATHER_URL='http://api.openweathermap.org/data/2.5/'
API_WEATHER_KEY='e5258c084f0922c874f5f0488d4a5fe4'

```
 * Para fins de teste, foi disponibilizado a chave e a URL da API externa utilizada
5\. Criar o banco de dados e aplicar as migrações:
```
python manage.py migrate
``` 
6\. Executar o servidor da aplicação:
```
python manage.py runserver
```

## Utilização
Uma vez que o servidor da aplicação está sendo executado, é possível acessar a API através da URL http://localhost:8000/api/.

Além disso, é possivel acessar a documentação da API através da URL http://127.0.0.1:8000/docs/.

 Aqui estão alguns exemplos de requisições que é possível realizar:

* `GET /api/estado`

* `POST /api/estado`

* `PUT /api/estado`

* `DELETE /api/estado`

* `GET /api/cidade`

* `POST /api/cidade`

* `PUT /api/cidade`

* `DELETE /api/cidade`

Também é possível realizar requisições do tipo GET com paginações, como por exemplo:

* `GET http://127.0.0.1:8000/api/estado?page=2&page_size=2`

* `GET http://127.0.0.1:8000/api/cidade?page=1&page_size=3`

Por fim, além do CRUD para estado e cidade foi desenvolvido um endpoint de clima para verificação do tempo para uma cidade passada por argumento via body, como por exemplo:
```
  POST http://127.0.0.1:8000/api/clima/
```
```json
body:
 {"nome": "londres"}
```
Se o local não existir no banco ou na API, é retornado um erro com status code: 404. Caso contrário, é retornado o tempo atual para cidade solicitada.