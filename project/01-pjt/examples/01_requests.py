# drive installed library
import requests

#jsonplaceholder: json data supply api
#requests는 get 요청으로 응답받은 데이터를 담은 객체에게
#json()이라는 메서드를 만들어두었다.
# #javascript 형식의 json 메서드를 파이써넹서 사용할 수 있도록
# python에서 사용할 수 있도록 파이썬이ㅡ data type에 맞게 변환해주는 메서드 
response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
user_reponse = requests.get('https://jsonplaceholder.typicode.com/users').json()

completed_todos = [] #final completed data list
fields = ['id','title']
for item in response:
    #Use only completed is True
    #if key is completed we only use value is True cases

    if item['completed'] == False:
        continue
    #    print(item)
    #if item.get('completed'):
    #    print(item)
    # in this items, gather id, title field that we need
    temp_item = {}
    for key in fields:
        #temp_item['id'] = item['id'] value
        temp_item[key] = item[key]

    for user in user_reponse:
        if user['id'] == item['userId']:
            user_info = {
                'id': user['id'],
                'name' : user['name'],
                'username' : user['username'], 
                'email' : user['email'],
            }
            temp_item['user'] = user_info

    completed_todos.append(temp_item)
print(completed_todos)

