import sys
# 입력 파일에서 읽기
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스 수

for test_case in range(T):
    K, N, M = map(int, input().split())  # 최대 이동거리 K, 종점 N, 충전소 개수 M
    stop_list = list(map(int, input().split()))  # 충전소 위치 리스트

    charge_count = 0  # 충전 횟수 초기화
    relative_location = []

    # 각 충전소까지 얼마나 가까운지를 저장 (K - station)
    for station in stop_list:
        relative_location.append(K - station)

    # 재귀 함수 정의
    def how_many_stops(charge_count, relative_location):
        continued = []  # 현재 턴에서 도달 가능한 정류장들

        # 더 이상 충전소가 없으면 종료 (정상 도착)
        if len(relative_location) == 0:
            print(f"#{test_case+1} {charge_count}")

        # 가장 가까운 충전소도 못 가면 실패
        elif relative_location[0] < 0:
            print(f"#{test_case+1} 0")

        # 마지막 충전소만 남은 경우
        elif len(relative_location) == 1:
            # 마지막 충전소에서 종점까지 갈 수 있는지 판단
            if relative_location[0] >= N - stop_list[-1]:
                print(f"#{test_case+1} {charge_count}")  # 현재 충전 없이 도달 가능
            elif relative_location[0] < N - stop_list[-1]:
                if N - stop_list[-1] <= K:  # 마지막 충전소에서 한번 더 충전해서 도달 가능
                    charge_count += 1
                    print(f"#{test_case+1} {charge_count}")
                else:
                    print(f"#{test_case+1} 0")  # 마지막 충전소에서도 도달 불가
            else:
                print(f"#{test_case+1} 0")  # 잘못된 경우 처리

        # 일반적인 경우
        else:
            # 현재 도달 가능한 충전소들을 continued에 저장
            for loc in relative_location:
                if loc >= 0:
                    continued.append(loc)
                else:
                    # 더 이상 못 가는 지점 도달 → 충전 필요
                    charge_count += 1
                    break

            # 도달한 충전소들을 잘라내고 남은 리스트만 사용
            relative_location[:] = relative_location[len(continued):]

            # 남은 충전소가 없지만 아직 도착 안 했을 경우 → 마지막 충전
            if len(relative_location) == 0:
                charge_count += 1

            # 남은 충전소들의 상대 거리 갱신
            for i in range(len(relative_location)):
                relative_location[i] += K - continued[-1]

            # 재귀 호출로 다음 라운드 진행
            how_many_stops(charge_count, relative_location)

    # 함수 호출 시작
    how_many_stops(charge_count, relative_location)
