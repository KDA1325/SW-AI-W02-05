class Solution:
    # x 거듭제곱 n -> x^n
    # x^1 -> x
    # x^2 -> x*x = a
    # x^3 -> x*x*x -> x^2 * x = ax
    # x^4 -> x*x*x*x -> x^2 * x^2 =a * a

# x^10 -> x^2 * x^2 * x^2 * x^2 * x^2 = a * a* a* a* a
    def myPow(self, x: float, n: int) -> float:
        a = x * x
        a_times = 0
        result = 0
        
        if n > 0:
            # if n % 2 == 0:
            #     a_times = n / 2

            #     print(a_times)

            #     # a를 a_times 곱함 
            #     for i in range(1, a_times+1):

            #         result = a * a_times


            #     # for i in range(1, n + 1):

            #     #     result = a * a_times 
                
            #     else:
            #         a_times = i / 2
            #         result = a * a_times * x
            
            # 파이썬 연산자 a ** b => a^b
            result = x ** n

        elif n == 0:
            result = 1

        elif n == 1: 
            result = x

        else: 
            x = 1 / x
            n = n * -1

            # 
            for i in range(1, n + 1):
                result = x * x  
        return result