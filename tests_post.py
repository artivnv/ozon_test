import requests

print('\n\nPOST1')
param = [('userId', '1'), ('title', 'foo'), ('body', 'bar')]
param2 = [('title', 'foo'), ('body', 'bar'), ('email', 'username@email.com'), ('username', 'admin'), ('name', 'Ervin Howell')]
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=param)
print("Код состояния:\n{}".format(response.status_code))
print("Записанные данные:\n{}".format(response.json()))
print("Следующий id в списке:\n{}".format(response.json()['id']))

print('\n\nPOST2')
param2 = [('title', 'foo'), ('body', 'bar'), ('email', 'username@email.com'), ('username', 'admin'), ('name', 'Ervin Howell')]
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=param2)
print("Код состояния:\n{}".format(response.status_code))
print("Записанные данные:\n{}".format(response.json()))
print("Следующий id в списке:\n{}".format(response.json()['id']))

print('\n\nPOST3')
param3 = [('', '')]
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=param3)
print("Код состояния:\n{}".format(response.status_code))
print("Записанные данные:\n{}".format(response.json()))
print("Следующий id в списке:\n{}".format(response.json()['id']))

