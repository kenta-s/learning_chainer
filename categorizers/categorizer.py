# You must install mecab before running this script.

# brew install mecab
# brew install mecab-ipadic
# pip install mecab-python3

import MeCab
mecab = MeCab.Tagger("-Ochasen")

text = mecab.parse("これはすごいテキストです")
