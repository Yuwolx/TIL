def hanoi(n, source, auxiliary, target):
    """
    n개의 원반을 source 기둥에서 target 기둥으로 옮깁니다.

    Args:
        n (int): 이동할 원반의 개수
        source (str): 시작 기둥 (예: 'A')
        auxiliary (str): 보조 기둥 (예: 'B')
        target (str): 목표 기둥 (예: 'C')
    """
    #일단 원반이 1개보단 많아야 한다
    if n > 0:
        # phase1: prepare for move biggest plate
        # n-1개 기둥 옮기기 -> 보조 기둥
        hanoi(n-1, source, target, auxiliary)

        #2단계: 목표였던 가장 큰 원반을 옮긴다

        # 3단계: 마무리 작업
        # 가장 큰 원반을 옮겼으니
        # 보조기둥에서 타겟 기둥으로 옮겨야 한다.
        hanoi(n-1,auxiliary,target)

# --- 실행 예시 ---
# 3개의 원반을 'A' 기둥에서 'C' 기둥으로 옮기기 ('B' 기둥을 보조로 사용)
number_of_disks = 3
hanoi(number_of_disks, 'A', 'B', 'C')