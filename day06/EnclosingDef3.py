# 嵌套函示 III

def make_lotto(n):
    def multi(x):
        return n * x
    return multi   #通常不太加括號，直接給物件就好

m3 = make_lotto(3)  #n = 3
m5 = make_lotto(5)  #n = 5

print(m3(6))  #multi呼叫時要給x參數  x = 6
print(m5(7))  #x = 7

print(m3(m5(2)))   # --> print(m3(10))

*******************
#閉包題目
def outer():
    x = 10
    def inner():
        print(x)
    x = 20
    return inner

f = outer()
f()  #會印出最後改變的參數