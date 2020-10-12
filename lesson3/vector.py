#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer

# コーパス情報を作成
corpus = {}
corpus["カレー"] = ["私", "は", "カレー", "が", "好き"]
corpus["ラーメン"] = ["私", "は", "ラーメン", "が", "好き"]

# 単語境界を一旦半角スペースとして
# TfidfVectorizer にかける配列の形状にする
docs = []
# ドキュメントの情報がタイトルからど
# この配列番号に保存されているかを保持する辞書
title2id = {}
cnt = 0
for title, tokens in corpus.items():
    # 配列を半角スペースで文字列結合
    # docs = [
    # "私 は カレー が 好き",
    # "私 は ラーメン が 好き"
    # ]
    # の形にする
    docs.append(" ".join(tokens))
    title2id[title] = cnt
    cnt += 1
    
# 1文字毎でも単語として扱う
# https://analytics-note.xyz/machine-learning/bow-tfidf-one-character/
vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')

# x[0]: 私 は カレー が 好き
# x[1]: 私 は ラーメン が 好き
# のデータがインデクスされているので各タイトルと入力データが何番目か事前に保存しておく必要がある
x = vectorizer.fit_transform(docs)

# ラーメンのtfidfベクトルを取得
ramen_vec = x[title2id["ラーメン"]].toarray()

print(ramen_vec)
