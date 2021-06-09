#裝飾器 3

def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def make_shoes(func):
    def shoes():
        print("穿鞋子")
        func()
    return shoes

@make_dress
@make_shoes
def out():
    print("我要出門了")

@make_shoes
def out2():
    print("我要出門了")

# john = make_dress((make_shoes(out))  #太過於複雜，可使用“簡化語法:@符號 + 裝飾器函數”，如上
john = out
john()

tom = out2
tom()
