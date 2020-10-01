#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 【td-idf】
#
import math

##
## 関数は基本的にフラットに定義していく
## また関数は入出力、処理を明確に実装していく
##

""" tokenの配列を辞書に変換する
    key は token で value は出現頻度
"""
def ary2dict(ary):
    dict = {}
    for t in ary:
        if not t in dict:
            dict[t] = 1
        else:
            dict[t] += 1
    return dict

""" tf 作成関数
    tf は以下の式で与えられる
    tf(t, d) = count(t) / count(d)
    ここでcount(t) は１つの文書に出現する任意のtoken の数
 　 ここでcount(d) は１つの文書に含まれるtoken の総数

　  以下の関数では１つの文書に含まれるtokenのリストを渡して
    各語彙毎のtfの値を計算する

    例)
　　・input
      tokens = ["a", "b", "a", "c"] である場合に
    ・output
      {"a": 0.5, "b": 0.25, "c": 0.25} 
"""
def tf(tokens):
    # token は１つの文書に含まれる語彙(token)のリスト(["f", "g", "c"])を入力として
    val = {}
    # 文書の中に含まれているtokenの数をd とする
    d = float(len(tokens))
    for t in tokens:
        if not t in val:
            val[t] = 1
        else:
            val[t] += 1
    for t, v in val.items():
        val[t] = float(v) / d
    return val

""" idf 作成関数
    idf 以下の式で与えられる
    idf = log(N/nij)

    ここでN は文書数
    nij はtokenの文書出現数 (DF)
"""
def idf(ds):
    # 総文書数
    n = float(len(ds))
    
    # 全文書からDF 辞書を作成:
    df = {}
    for title, tokens in ds.items():
        for t in set(tokens):
            print(t)
            if not t in df:
                df[t] = 1
            else:
                df[t] += 1
    # idf辞書            
    ret = {}
    for t, v in df.items():
        ret[t] = math.log(n/v)
    return ret


"""tfidf に変換する"""
def tfidf(vec, idf_dict):
    ret = {}
    tf_dict = tf(vec)    
    for t, tf_score in tf_dict.items():
        ret[t] = tf_score * idf_dict[t]
    return ret

def norm(vec):
    n = 0.0
    for _, x in vec.items():
        n += (x*x)
    return math.sqrt(n)

def dot(vec1, vec2):
    val = 0.0
    for t, x in vec1.items():
        if t in vec2:
            val += x * vec2[t]
    return val

def cosine_similarity(v1, v2):
    sim = dot(v1, v2) / (norm(v1) * norm(v2))
    return sim

# 文書の持ち方を以下のように修正
# 辞書型(dictionary) で保存する
# 辞書の key に タイトル名("x","y","z"とするこれはタイトル、文字列)
# 辞書の value に token 情報 (分かち書きされたトークン情報を配列で持つ)
#
# 例)
# key:  "ラーメン"
# value: ["ラーメン", "と", "は", "中華", "麺", "と"・・・]
#

# 文書集合の辞書の初期化
ds = {} 

# 文書x: タイトルを x とする
ds["x"] = ary2dict(["a", "b", "c","b","a","d","e","a","z"])

# 文書y: タイトルを y とする
ds["y"] = ary2dict(["c", "d", "e","b","a","d"])

# 文書z: タイトルを z とする
ds["z"] = ary2dict(["f", "g", "c"])

print(ds)

# IDF 辞書を作成
idf_dict = idf(ds)
      
# 文書x, 文書y の類似度を計算する
x_tfidf = tfidf(ds["x"], idf_dict)
y_tfidf = tfidf(ds["y"], idf_dict)

sim = cosine_similarity(x_tfidf, y_tfidf)
print(sim)
