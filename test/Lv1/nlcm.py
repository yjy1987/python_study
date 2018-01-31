def nlcm(num):
    # 순서대로 정렬
    # 왜 .sort()는 안되는걸까
    answer = sorted(list(num),key=int)

    # 리스트 answer를 받아서 for문을 돌린다
    res = []
    for i in answer:
        res.append(list(filter(lambda x:x%i==0 and x%i!=1, answer)))




    return res

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,14,8]));