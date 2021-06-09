#裝飾器 1

def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress


def out():
    print("我要出門了")


john = make_dress(out)  #先穿衣服再出去
john()