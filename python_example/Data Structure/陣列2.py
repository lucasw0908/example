pokemon = ["妙蛙種子", "小火龍", "傑尼龜"]

pokemon.append("皮卡丘")
print(pokemon)
# >>['妙蛙種子', '小火龍', '傑尼龜', '皮卡丘']

pokemon.insert(1, "綠毛蟲")
print(pokemon)
# >>['妙蛙種子', '綠毛蟲', '小火龍', '傑尼龜', '皮卡丘']

pokemon.remove("綠毛蟲")
print(pokemon)
# >>['妙蛙種子', '小火龍', '傑尼龜', '皮卡丘']

pokemon.pop(1)
print(pokemon)
# >>['妙蛙種子', '傑尼龜', '皮卡丘']

pokemon.reverse()
print(pokemon)
# >>['皮卡丘', '傑尼龜', '妙蛙種子']