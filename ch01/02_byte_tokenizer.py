# 'A' の場合
# 属于**字符串（str）对象的方法**，不是内置函数，作用： **str（Unicode 字符串） → bytes（字节串）**
encoded = 'A'.encode("utf-8")
print(encoded)        # b'A'
print(list(encoded))  # [65]

# 'あ' の場合
encoded = 'あ'.encode("utf-8")
print(encoded)        # b'\xe3\x81\x82'
print(list(encoded))  # [227, 129, 130]

ids = [65]
decoded = bytes(ids).decode("utf-8")
print(decoded)   # 'A'


class ByteTokenizer:
    def encode(self, text):
        return list(text.encode("utf-8"))

    def decode(self, ids):
        return bytes(ids).decode("utf-8")


# 使用例
tokenizer = ByteTokenizer()
text = "hello世界😁"

# エンコード
ids = tokenizer.encode(text)
print(ids)  # [104, 101, 108, 108, 111, 228, 184, 150, 231, 149, 140, 240, 159, 152, 129]

# デコード
decoded = tokenizer.decode(ids)
print(decoded)  # hello世界😁