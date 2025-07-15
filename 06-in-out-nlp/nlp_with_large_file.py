import re

# 你不用太关心这个函数
def parse(file_path):
    word_cnt = {}
    chunk_size = 1024 * 4  # 每次读取1MB
    with open(file_path,'r') as fin:
        while True:
            text = fin.read(chunk_size)
            if not text:
                break
            # 使用正则表达式去除标点符号和换行符
            text = re.sub(r'[^\w ]', ' ', text)

            # 转为小写
            text = text.lower()

            # 生成所有单词的列表
            word_list = text.split(' ')

            # 去除空白单词
            word_list = filter(None, word_list)

            # 生成单词和词频的字典
            for word in word_list:
                if word not in word_cnt:
                    word_cnt[word] = 0
                word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt

word_and_freq = parse("in.txt")

with open('out1.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))