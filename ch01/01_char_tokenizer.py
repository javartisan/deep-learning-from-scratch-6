text = "hello世界😁"
print(list(text))  # ['h', 'e', 'l', 'l', 'o', '世', '界', '😁']

# ## 1. `ord(c)`
# **全称：ordinal**
# 作用：接收**单个字符**，返回它对应的 Unicode 整数编码。
print(ord('h'))  # 104
print(ord('😁'))  # 128513

# ## 2. `chr(n)`
#
# 作用：接收**整数编码**，返回对应的字符。
print(chr(104))  # 'h'
print(chr(128513))  # '😁'

ids = [ord(char) for char in list(text)]
print(ids)  # [104, 101, 108, 108, 111, 19990, 30028, 128513]


class CharTokenizer:
    def encode(self, text):
        return [ord(char) for char in text]

    def decode(self, ids):
        return ''.join([chr(i) for i in ids])


tokenizer = CharTokenizer()
text = "hello世界😁"

# エンコード
ids = tokenizer.encode(text)
print(ids)  # [104, 101, 108, 108, 111, 19990, 30028, 128513]

# デコード
decoded = tokenizer.decode(ids)
print(decoded)  # hello世界😁
