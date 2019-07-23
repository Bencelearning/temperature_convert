def c_f(c): #攝氏溫度轉換華氏溫度
    f = float(c) * 9 / 5 + 32
    print('攝氏溫度', str(c), '的華氏溫度為', str(f))
def f_c(f): #華氏溫度轉換攝氏溫度
    c = (float(f) - 32) * 5 / 9
    print('華氏溫度', str(f), '的攝氏溫度為', str(c))
    
while True:
    mode = input('請選擇轉換模式, 輸入 1 為攝氏轉換華氏, 輸入 2 為華氏轉換攝氏, 輸入 3 結束程式\n')
    if mode == '1':
        while True:
            c = input('請輸入一攝氏溫度值, 若輸入"b"則返回模式選擇\n')
            if c == 'b':
                break
            else:
                try:
                    c_f(c)
                except ValueError:
                    continue
    elif mode == '2':
        while True:
            f = input('請輸入一華氏溫度值, 若輸入"b"則返回模式選擇\n')
            if f == 'b':
                break
            else:
                try:
                    f_c(f)
                except ValueError:
                    continue
    elif mode == '3':
        print('bye')
        break
    else:
        print('要離開就輸入 3 啦')
        continue