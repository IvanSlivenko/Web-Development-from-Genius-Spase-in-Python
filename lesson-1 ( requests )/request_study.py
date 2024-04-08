import requests

site = "https://jsonplaceholder.typicode.com/posts"
#------------------------------------------------------------------------- get
print("-------------- get")# ------------------ Отримуємо
# response_get = requests.get(url=site+"/1")
# print(response_get)  # отримуємо статус - код відповіді
# print(response_get.text)  # отримуємо текст

# print(response_get.json())  # отримуємо текст у форматі json
# print("title :", response_get.json()["title"])
# print("userId :", response_get.json()["userId"])
# print(response_get.headers)
# ============================================================
# for header, value in response_get.headers.items():
#     print(f"Header: {header} --> Value: {value}")
# ============================================================
#------------------------------------------------------------------------- post
print("-------------- post")#-------------------Додаємо
# body = {
#     "userId": 12,
#     "title": "test",
#     "body": "test"
# }
#
# headers = {
#     "Content-Type": "application/json; charset=utf-8"
#
# }
#
#
# response_post = requests.post(url=site, json=body, headers=headers)
# print(response_post.status_code)
# print(response_post.reason)
# print(response_post.text)
print("-------------- put")#--------------------Змінюємо те, що було на те, що буде (все на все)
#
# data_put = {
#     "title": "test_put",
#
# }
# response_put = requests.put(url=site+"/1", data=data_put)
# print(response_put.status_code)
# print(response_put.reason)
# print(response_put.text)

print("------------------patch")#-------------- Змінюємо тільки ті поля, що вказали
# data_patch = {
#     "title": "test_patch",
#
# }
# response_patch = requests.patch(url=site+"/1", data=data_patch)
# print(response_patch.status_code)
# print(response_patch.reason)
# print(response_patch.text)

print("----------------- delete")#------------- Видаляємо
# response_delete = requests.delete(url=site+"/1")
# print(response_delete.status_code)
# print(response_delete.reason)
# print(response_delete.text)

print("--------------------------------------")






