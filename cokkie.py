import requests

#if response.status_code == 200:
#response.raise_for_status()

#print(response) #вывести весь текст print("response.text)

#переходим к наши заголовкам

headers = {
    "User-Agent": "IT_OVERONE"
}

website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())
#response = requests.post ("https://httpbin.org/post", headers = headers,
#                        params = {"a":"b"},
#                        json = {"username": "secret"})

response = requests.delete(website, data = {
    "Id": 1,
    "userId": 12,
    "tittle": "my new post",
})

#передаем аргументы с помощью ?a=b
#отправляем данные с помощью post, меняем везде где get на json

#print(response.text)
#print(response.json())
#для простоты удаления status_code
print(response.status_code)