import allure
import requests


@allure.feature('create user')
def test_create_user():
    response = requests.post('https://reqres.in/api/users', data={
        'name': 'Ivan Ivanov',
        'job': 'Driver'
    })
    assert response.status_code == 201

    print(response.json())

    assert 'id' in response.json()


@allure.feature('update_user')
def test_update_user():
    response = requests.put('https://reqres.in/api/users/2', data={
        'name': 'Ivan Ivanov',
        'job': 'Driver'
    })

    assert response.status_code == 200

    print(response.json())

    assert response.json()['name'] == 'Ivan Ivanov'
    assert response.json()['job'] == 'Driver'


@allure.feature('delete_user')
def test_delete_user():
    response = requests.get('https://reqres.in/api/users')
    user_list = response.json()['data']
    user_id = None
    for user in user_list:
        if user['id'] == 2:
            user_id = 2
            break
    assert user_id is not None, "Данный пользователь не найден"

    response = requests.delete(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 204


@allure.feature('single_user')
def test_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["last_name"] == "Weaver"


@allure.feature('list_resources')
def test_list_resources():
    response = requests.get(f"{'https://reqres.in/api'}/unknown")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data["data"]) == 6


@allure.feature('single_resource')
def test_single_resource():
    response = requests.get(f"{'https://reqres.in/api'}/unknown/2")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["data"]["id"] == 2
    assert data["data"]["name"] == "fuchsia rose"
    assert data["data"]["year"] == 2001
    assert data["data"]["color"] == "#C74375"


@allure.feature('test_register')
def test_register():
    response = requests.post('https://reqres.in/api/register', data={
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    })
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data['token'] == 'QpwL5tke4Pnpja7X4'


@allure.feature('test_login')
def test_login():
    response = requests.post('https://reqres.in/api/login', data={
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    })
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data['token'] == 'QpwL5tke4Pnpja7X4'


@allure.feature('delayed_response')
def test_delayed_response():
    response = requests.get('https://reqres.in/api/users?delay=3')
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert 'data' in data


@allure.feature('resource_not_found')
def test_resource_not_found():
    response = requests.get('https://reqres.in/api/unknown/23')
    assert response.status_code == 404
