def sumMatrix(A, B):
    answer = [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))