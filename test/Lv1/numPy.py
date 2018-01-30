def numPY(s):
    # 함수를 완성하세요
    a = s.lower()
    res = False
    if (list(a).count('p') == list(a).count('y')):
        res = True
    else:
        res = False
    return res


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("IzPPyyc"))
#print(numPY("dYYYPPELTZ"))