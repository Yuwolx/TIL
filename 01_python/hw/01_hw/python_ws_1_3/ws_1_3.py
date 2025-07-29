users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.
# 문제

# 제공된 SNS 사용자 데이터를 기반으로 특정 조건을 만족하는 사용자 정보를 필터링하고, 
# 이를 함수와 모듈을 사용하여 구현하시오.

# 요구사항

# 나이가 18세 이상인 사용자를 필터링하는 함수를 작성하시오.
def young_users(users):
    result = []
    for i in users:
        i['age'] >= 18
        result.append(i)
    return result

filtered_users = young_users(users)
print(filtered_users)

# 활성화된(is_active가 True인) 사용자를 필터링하는 함수를 작성하시오.

def active_users(users):
    result = []
    for user in users:
        if user["is_active"] == True:
            result.append(user)
    return result

actives = active_users(users)

for line in actives:
    print(line)

# 나이가 18세 이상이고 활성화된 사용자를 필터링하는 함수를 작성하시오.

def old_active(users):
    result = []
    for user in users:
        if user['age'] >= 18 and user['is_active'] == True:
            result.append(user)
    return result

old_active_users = old_active(users)
print(old_active_users)


# 위의 함수를 별도의 모듈로 작성하고, 이를 메인 파일에서 불러와 사용하시오.

