def strip_and_lowercase(text):
    """
    문자열의 앞뒤 공백을 제거하고, 소문자로 변환한 문자열을 반환한다.
    """
    #make new list for save result
    result_list = []
    for i in text:
        i.strip() # eliminate blank 
        i.lower() # make small word
        result_list.append(i) #insert to new list
    return result_list # return modified word list


def is_valid_log(text):
    """
    로그 항목이 유효한지 검사한다.
    유효하지 않은 경우는 다음 조건 중 하나라도 해당되는 경우이다.
    - 공백 문자열
    - "error" 또는 "none" 이 포함된 문자열
    - 숫자로만 구성된 문자열
    """
    regular_list =  []
    for i in text:
        if type(i) == int: # if text type is int, do not append to result list. But in example list '1234' type is string. So, certainly this approach is wrong.
            pass
        elif i in '': # if text consist only space do not appedn. but I forgot how to check wether valid or not
            pass
        elif i in ['error','none']:
            pass
        else:
            regular_list.append(i)

    return regular_list




def clean_log(text):
    """
    '_'가 포함된 경우 이를 ' '로 바꾸고,
    각 단어의 첫 글자를 대문자로 바꾼다. (Title Case)
    """
    results_list = [] #new list for function
    for i in text:
        i.split(' ') #devide by space for make large every first letter
        for x in i:
            new_word = []
            x.capitalize() #make large word: first letter
            new_word.append(x) # corporate again for initial word
        results_list.append(i)
    return results_list


def process_logs(log_list):
    """
    전체 로그 리스트를 받아 유효한 항목만 정제하여 리스트로 반환한다.
    위 함수들을 적절히 활용해야 한다.
    """
    log_list = strip_and_lowercase(log_list) #cleaner
    log_list = is_valid_log(log_list)        #fillter
    log_list = clean_log(log_list)           #cleaner
    return log_list



# 아래 코드는 수정 할 수 없음
raw_logs = [
    "  user_login  ",
    "ERROR_404",
    "   page_viewed",
    "None",
    "signup_success ",
    "  1234 ",
    "   ",
]

result = process_logs(raw_logs)
print(result)
# ['User login', 'Page viewed', 'Signup success']
