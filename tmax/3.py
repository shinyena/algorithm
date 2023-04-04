def is_palindrome(number):
    number = list(str(number))
    idx = 0
    while idx<len(number)//2:
        if number[idx] != number[len(number)-1-idx]:
            return False
        idx += 1
    return True

def solution(remittance):
    answer = []
    for r in remittance:
        num = r
        while not is_palindrome(num):
            num += 1
        answer.append(num)
    return answer

print(solution([8000, 199992, 11011]))
print(solution([1, 102, 10, 99, 100]))