# You must install mecab before running this script.

# $ brew install mecab
# $ brew install mecab-ipadic
# $ pip install mecab-python3

# And gensim
# $ pip install gensim

import MeCab
from gensim import corpora

mecab = MeCab.Tagger("-Ochasen")

mecab.parse('') # まずいタイミングでtextがGCされるらしくてmecabがエラー吐く問題を対処するハック。これは酷い。

text = "【ナダル快挙 感動表現できない】「赤土の王者」ナダルが全仏10度目のV。「今は感動ばかりで言葉が見つかりません」と優勝杯を力強く抱きかかえ、会心の笑顔。"
node = mecab.parseToNode(text)

words = []
while node:
    meta = node.feature.split(",")
    if meta[0] == "名詞":
        words.append(node.surface)
    node = node.next

dictionary = corpora.Dictionary([words])
print(dictionary.token2id)

# from IPython import embed
# from IPython.terminal.embed import InteractiveShellEmbed
#
# embed()
