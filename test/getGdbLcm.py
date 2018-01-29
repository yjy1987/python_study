import timeit
def gcdlcm(a, b):
    if a > b:
        max = a
        min = b
    elif a < b:
        max = b
        min = a
    else:
        max = a
        min = a

    gcd = 0
    lcm = 0
    for i in range (min, 0, -1):
        if (min%i==0 and max%i==0) :
           if(i>1):
               gcd=i
               lcm=int(min * max / gcd)
           else:
               gcd=1
               lcm=min*max
           break
    array = [gcd,lcm]
    return array


# 아래는 테스트로 출력해 보기 위한 코드입니다.

print(gcdlcm(3, 12))



