def nextSqure(n):
    # 함수를 완성하세요


    return ((n**.5)+1)**2 if int(n**.5)-n**.5==0 else 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));