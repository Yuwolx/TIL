def clean_name(name):
    """
    이름의 앞뒤 공백을 제거하고, 첫 글자만 대문자로 바꿉니다.
    (예: "  heLLo " -> "Hello")
    """
    name = name.strip()
    name = name.capitalize()
    return name
   
def make_greeting(name):
    """
    정리된 이름을 받아 "안녕하세요, [이름]님!" 형식의 문자열로 만듭니다.
    (예: "홍길동" -> "안녕하세요, 홍길동님!")
    """
    name = clean_name(name)
    return f"Hello, mr/s {name}!"

def process_namelist(name_list):
    """
    전체 이름 리스트를 받아, 비어있지 않은 이름만 골라 인사말로 만들어
    리스트로 반환합니다.
    (이름이 공백으로만 이뤄진 경우는 무시합니다.)
    위에 작성한 함수들을 적절히 활용해야 합니다.
    """
    names = []
    for i in name_list:
        if i.strip():
            x = make_greeting(i)
            names.append(x)

    return names


# ----------------------------------------------------
# 아래 코드는 절대 수정하지 마시오.
# ----------------------------------------------------
raw_names = [
    "  홍길동",
    "김싸피 ",
    "   ",
    "lee sunsin"
]
result = process_namelist(raw_names)
print(result)