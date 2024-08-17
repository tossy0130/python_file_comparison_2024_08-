# ratioで、２つの文字列の類似度を算出
import difflib

fruits1 = 'Apple Banana Orange Peach Mango'
fruits2 = 'Apple Banana Peach Mango Orange Grape'
fruits3 = 'Apple Banana Orange Peach Grape'
fruits4 = 'Apple Banana Orange Peach Mango'

tel = '090-5555-8888'
tel2 = '090-5555-9999'

s12 = difflib.SequenceMatcher(None, fruits1, fruits2)
print(s12.ratio())
# 結果： 0.7058823529411765

s13 = difflib.SequenceMatcher(None, fruits1, fruits3)
print(s13.ratio())
# 結果：0.8709677419354839

s14 = difflib.SequenceMatcher(None, fruits1, fruits4)
print(s14.ratio())
# 結果：1.0

# 比較した結果で分岐させる。
if s14.ratio() == 1.0:
    print('OK')
else:
    print('NG')

# ========================= tel , tel2 の比較
sTel01 = difflib.SequenceMatcher(None, tel, tel2)
print(sTel01.ratio())
