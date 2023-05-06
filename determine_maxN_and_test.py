#以純粹遞迴方式求F(n)的演算法
def F(n):
    if n <= 1:
        return n
    return F(n-1) + F(n-2)

#以動態規劃方式求F(n)的演算法，其中使用字典來記錄F(n)，使用memo[n]可獲取其值
def Fib_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = Fib_dynamic(n - 1) + Fib_dynamic(n - 2)
    memo[n] = result
    return result

#初始化參數
n = 1
low = 0
upper = 0
#n為執行F(n)不會導致電腦崩潰(爆炸)的最大值，為一正整數
#第一個迴圈先訂出n可能所在區間
while True:
    try:
        F(n+1) 
        n *= 2
    except RecursionError:  #利用例外處理來判斷F(n)是否導致電腦崩潰
        upper = n   #n的上界，因為F(n+1)確定爆
        low = (n//2)+1  #n的下界，因為F((n//2)+1)確定不爆，是已知不會爆的n的最大值
        break
#第二個迴圈利用二分搜尋法快速找到n
while low < upper:
    mid = (low + upper)//2
    try:
        F(mid+1) 
        low = mid+1
    except RecursionError:
        upper = mid
n = upper
print("The maximum value of n is:", n)
#使用動態規劃演算法看看F(n+1)是否跟純粹遞迴演算法一樣會爆炸
try:
    Fib_dynamic(n+1)
    print("Success!")
except RecursionError:
    print("BOOM!!!")
