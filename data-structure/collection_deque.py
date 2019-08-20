from collections import deque


if __name__ == "__main__":
    q = deque(["버피", "잰더", "윌로"])
    q.append("자일스")
    print(q.popleft())
    print(q.pop())
    print(q)
    q.appendleft("엔젤")
    print(q)
