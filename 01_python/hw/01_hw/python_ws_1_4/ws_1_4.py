
# 요구사항
# movies 리스트에 'Inception', 'Interstellar', 'Dunkirk', 'Tenet' 문자열을 추가한다.
movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']

# get_movie_recommendation 함수를 정의하여, rating 매개변수를 받아서 다음과 같은 조건에 따라 영화를 추천한다:
def get_movie_recommendation(rating):
    if rating >= 9:
        print('Inceoption')
    elif rating >= 8:
        print('Interstellar')
    elif rating >= 7:
        print('Dunkirk')
    else:
        print('Tenet')

# rating이 9 이상이면 'Inception'을 추천한다.

# rating이 8 이상 9 미만이면 'Interstellar'를 추천한다.

# rating이 7 이상 8 미만이면 'Dunkirk'를 추천한다.

# 그 외의 경우 'Tenet'을 추천한다.

# 영화 평점을 사용자로부터 터미널에서 입력받아, get_movie_recommendation 함수를 호출하여 추천 영화를 출력한다.
rating = int(input())

get_movie_recommendation(rating)