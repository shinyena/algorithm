# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 40ms

n = int(input())
que1 = "\"재귀함수가 뭔가요?\""
que2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
que3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
que4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
ans1 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
ans2 = "라고 답변하였지."

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def recursion(i):
    print("____" *i + que1)
    if i==n:
        print("____" *n + ans1)
    else:
        print("____"*i + que2)
        print("____"*i + que3)
        print("____"*i + que4)
        recursion(i+1)
    print("____"*i + ans2)

recursion(0)