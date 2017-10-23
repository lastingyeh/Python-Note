# func
# 設定 default 參數
def test(c, p) -> (str, str):
    return c, p


# 參數若不同 需定義 default參數預設值
value = test('test', 'value')

print('return value', value)
