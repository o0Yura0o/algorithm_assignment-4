import time
import matplotlib.pyplot as plt
#以純粹遞迴方式求F(n)的演算法
def Fib_recursive(n):
    if n <= 1:
        return n
    return Fib_recursive(n - 1) + Fib_recursive(n - 2)

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

N_MAX = 100 #輸入欲求n之最大值，會自動轉為10的倍數
n_max = (N_MAX//10)*10+1
#產生一組n值清單，皆為10的倍數，最大值為(N_MAX//10)*10
n_values = list(range(10, n_max, 10))
#兩個清單用以分別儲存純粹遞迴演算法以及動態規劃演算法的執行時間
recursive_times = []
dynamic_times = []
#產生一個常數c，其值透過純粹遞迴演算法計算F(50)的執行時間得出
c = 4618/2**50
for i, n in enumerate(n_values):
    #為節省執行時間，n>=50以上的執行時間測量將不實際執行純粹遞迴演算法
    if n>=50:
        #已知使用純粹遞迴方式求算費氏數列的演算法其實間複雜度為Big_Oh(2^n)
        #所以實際執行時間可以透過一常數c乘上2^n求得，c透過觀察F(50)純粹遞迴演算法實際求解用時訂出
        execution_time = c*2**n 
        recursive_times.append(execution_time)
    else:
        #計算純粹遞迴演算法執行時間
        start_time = time.time()
        Fib_recursive(n)
        recursive_times.append(time.time() - start_time)
    
    #計算動態規劃演算法執行時間
    start_time = time.time()
    Fib_dynamic(n)
    dynamic_times.append(time.time() - start_time)

#利用折線圖視覺化結果
plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of F(n) Calculation')
plt.legend()
plt.show()
