num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1

# LEGB rule
# Local
# En-Cosed
# global
# Built-in

def outer_function():
    x = 0

    def inner_function():
        x = 10
        print(x)

    inner_function()
    print(x)
x = 10