from collections import defaultdict


def count_pairs(ids):
    counts = defaultdict(int)
    for pair in zip(ids, ids[1:]):
        counts[pair] += 1
    return counts


# 使用示例
ids = [1, 2, 3, 1, 2]
counts = count_pairs(ids)
print(counts)  # {(1, 2): 2, (2, 3): 1, (3, 1): 1}


def merge(ids, pair, new_id):
    merged_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
            merged_ids.append(new_id)
            i += 2
        else:
            merged_ids.append(ids[i])
            i += 1
    return merged_ids


# 使用示例
ids = [1, 2, 3, 1, 2]
merged = merge(ids, (1, 2), 4)
print(merged)  # [4, 3, 4]


def train_bpe(text, vocab_size):
    # 将文本转换为0~255的ID序列
    ids = list(text.encode("utf-8"))

    # 确定合并次数
    num_merges = vocab_size - 256  # 256是初始词汇表大小
    merge_rules = {}

    for step in range(num_merges):
        # 统计相邻配对的出现频次
        counts = count_pairs(ids)

        # 没有配对时的处理逻辑
        if not counts:
            break

        # 选出出现频率最高的配对
        best_pair = max(counts, key=counts.get)
        # best_pair = max(counts, key=lambda pair: (counts[pair], pair[0], pair[1]))

        # 分配新的token ID
        new_id = 256 + step
        merge_rules[best_pair] = new_id

        # 执行合并操作
        ids = merge(ids, best_pair, new_id)

    return merge_rules


# 使用示例
text = "Hello world! This is BPE training."
merge_rules = train_bpe(text, vocab_size=260)
print(merge_rules)  # {(105, 115): 256, (256, 32): 257, (105, 110): 258, (72, 101): 259}
