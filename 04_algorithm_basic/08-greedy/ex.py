def backtrack(path):
    print(f"👉 들어옴: path = {path}")

    # 🎯 정답 조건
    if len(path) == 2:
        print(f"✅ 길이 2 완성! path = {path}")
        return

    for num in [1, 2, 3]:
        print(f"➕ 선택: {num} → path + [{num}]")
        path.append(num)

        backtrack(path)  # 다음 자리 채우러 들어감

        print(f"🔙 되돌리기 전: path = {path}")
        path.pop()       # 백트래킹
        print(f"↩️ 되돌림 후: path = {path}")

backtrack([])
