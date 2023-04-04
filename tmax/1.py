def solution(teamIDs, additional):
    answer = []
    for a in additional:
        if a not in teamIDs and a not in answer:
            answer.append(a)
    return answer

print(solution(["world", "prog"], ["hello", "world", "code", "hello", "try", "code"]))
print(solution(["abc", "hq", "xyz"], ["hq", "abc", "pp", "xy", "pp", "hq"]))