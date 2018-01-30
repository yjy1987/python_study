def numPY(s):
    # 함수를 완성하세요

    return  True if (list(s).count('y') == list(s).count('p')) or (list(s).count('y')==0 and list(s).count('p')==0) else False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))