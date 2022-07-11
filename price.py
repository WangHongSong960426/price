print('計算商品 賺 或 虧 ')
dl = input('請輸入 !price! 啟動計算系統: ')

if dl == '!price!':
    while True:
        z = input('是否退出? ')
        if z == '是':
            break
        elif z == '否':
            op = float(input('你的商品成本多少元? '))
            tp = float(input('打折前商品價格多少元? '))
            s = int(input('商品要打幾折? '))
            if s < 10:
                s = s * 0.1
            elif s > 10:
                s = s * 0.01
            if tp * s > op:
                w = (tp * s) - op
                print('商品賺', w, '元')
            elif tp * s == op:
                w = (tp * s) - op
                print('商品沒有賺，也沒有虧')
            else:
                w = op - (tp * s)
                print('商品虧', w, '元')
        else:
            print('只能輸入 是 或者是 否 !')
else:
    print('只能打 !price!')