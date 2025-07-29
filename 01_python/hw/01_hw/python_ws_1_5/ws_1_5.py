# 아래에 코드를 작성하시오.
movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]

# 요구사항
# movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 새로운 리스트에 담는다.
# get_high_rated_movies 함수를 정의하여, threshold 매개변수를 받아서 평점이 threshold 이상인 영화를 리스트로 반환한다.
# 사용자로부터 평점 기준을 입력받아, get_high_rated_movies 함수를 호출하여 해당 평점 이상인 영화를 출력한다.

movies_dict = []
for title in range(len(movies)):
    movies_dict.append({'title' : movies[title], 'rating': ratings[title]})

def get_high_rated_movies(threshold):
    result = []
    for i in movies_dict:
        if i['rating'] >= threshold:
            result.append(i['title'])
    return result
        
threshold = int(input())
high_rate_movie = get_high_rated_movies(threshold)
print(high_rate_movie)

