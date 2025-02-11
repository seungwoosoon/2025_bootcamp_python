# v1.1 while 사용
def is_prime(num):
    if num < 2:
        return False  # 2 미만의 숫자는 소수가 아님

    i = 2
    while i * i <= num:  # i가 num의 제곱근 이하일 때까지만 반복
        if num % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
        i += 1  # 다음 숫자로 이동

    return True  # 모든 검사를 통과하면 소수


n = int(input("select num "))
if is_prime(n):
    print(f"{n}은 소수입니다")
else:
    print(f"{n}은 소수가 아닙니다",n)

# v1.2 while 구간 소수 출력 
# def is_prime(num):
#     if num < 2:
#         return False  # 2 미만의 숫자는 소수가 아님

#     i = 2
#     while i * i <= num:  # i가 num의 제곱근 이하일 때까지만 반복
#         if num % i == 0:
#             return False  # 나누어 떨어지면 소수가 아님
#         i += 1  # 다음 숫자로 이동

#     return True  # 모든 검사를 통과하면 소수

# n = int(input("select num "))
# num = 2
# while(num<=n):
#     if (is_prime(num)):
#         print(num, end=" ")
#     num = num+1


# v1.3 ** pow
# def is_prime(num):
#     if (num < 2):
#         return False
#     for i in range(2,int(pow(num,0.5)+1)):
#         if num % i == 0:
#             return False
#     return True
    

# n = int(input("select num "))
# num = 2
# while(num<=n):
#     if (is_prime(num)):
#         print(num, end=" ")
#     num = num+1

