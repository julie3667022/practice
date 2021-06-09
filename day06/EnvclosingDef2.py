# 嵌套函示 II

def calc_bmi(h, w):
    if h <= 0:
        return False

    def get_bmi():
        bmi = w / ((h/100)**2)
        return bmi

    return get_bmi

def compare_bmi(a, b):
    print(a(), b(), a() > b())

bmi1 = calc_bmi(170, 60)
bmi2 = calc_bmi(180, 90)
compare_bmi(bmi1, bmi2)



h = 170
w = 60
bmi = calc_bmi(h, w)
print(bmi())  #只打print(bmi)會跑出<function calc_bmi.<locals>.get_bmi at 0x7f954309ee50>
