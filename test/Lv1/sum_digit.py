def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''

    a = list(str(number))
    sum = 0
    for i in a:
        sum+=int(i)

    return sum
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));