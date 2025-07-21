'''
모든 학생의 평균 점수를 계산하여 출력하시오.
80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.
'''

'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

#1 아래에 코드를 작성하시오.
students = {'Alice':85, "Bob":78, "Charlie":92,
                 "David": 88, "Eve": 95}
print(type(students))
print("학생들의 이름과 점수:", students)
scores_list = students.values()
names = students.keys()

#2 Average of recods
a = 0
for i in scores_list:
    a += i

avg_records = a/len(scores_list)
print("모든 학생의 평균 점수: ", avg_records)


#3 extract names who get score more than 80
'''
best = []
dot = 80
for i in names:
    if students[i] >= dot:
       best.append(i)
       
print(f"기준점수 ({dot})점 이상을 받은 학생 수", best)
'''

#3.1 List Comprehension
dot = 80
best_students = [x for x in names if students[x] >= dot]
print(f"기준점수 ({dot})점 이상을 받은 학생 수", best_students)


#4 Print records ordered by descending
sorted_scores = sorted(students.items(), key=lambda x: x[1], reverse=True)

for name, score in sorted_scores:
    print(f"{name}:", score)
          
    
#5 gap, top to last score
x = 0
for i in scores_list:
    if i > x:
        best_score = i
        x = i

y = 100
for i in scores_list:
    if i < y:
        low_score = i
        y = i
print("점수가 가장 높은 학생과 낮은 학생의 점수 차이: ", best_score - low_score)

# Jedgement each student score with avg score
for i in names:
   if students[i] > avg_records:
       print(f"{i} 학생의 점수({students[i]})는 평균 이상입니다")
   else:
       print(f"{i} 학생의 점수({students[i]})는 평균 이하입니다")




