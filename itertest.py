# 因数を返すイテレータクラス
class PrimeFactor(object):
    # number で対象の数を、 max_count で返す因数の数を指定する
    def __init__(self, number, max_count):
        self.number = number
        self.max_count = max_count
        
    # インスタンスをジェネレータ化する
    def __iter__(self):
        count = 0
        for i in range(2, self.number):
            if self.number % i == 0:
                count += 1
                # 指定された数だけ因数が返されたらイテレータ処理を終了するために StopIteration() 例外をあげる
                if count > self.max_count:
                    raise StopIteration()
                yield i

pf = PrimeFactor(number = 100, max_count = 5)

# 1 周目
for n in pf:
    print(n, end=", ")
print()
# => 2, 4, 5, 10, 20,

# 2 周目
for n in pf:
    print(n, end=", ")
print()
# => 2, 4, 5, 10, 20,
