#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 日本語の文字列正規化ライブラリとして定番
# https://pypi.org/project/mojimoji/
#
# ```
# pip3 install mojimoji
# ```
import mojimoji
import glob

# いらない文字を削除するトリミング関数
def triming(text):
    text = text.replace("\r\n", "")
    text = text.replace("\n", "")
    text = text.replace("\t", " ") # tab文字列 は 半角
    text = text.replace('\u3000', "")
    return text

def normalize(text):
    # 全角文字を半角へ変換(カナなどは対象外)
    return mojimoji.zen_to_han(text, kana=False)

def map_lines(file_list):
    output_files = []
    for file in file_list:
        texts = []
        with open(file, 'r') as fd:
            # 1ファイルの中身を全部読み込み
            # 最初の2行はヘッダ的な情報なので必要なし
            lines = fd.readlines()[2:]
            for line in lines:
                if line.strip() == "":
                    continue
                # トリミング＆正規化
                text = normalize(triming(line))
                if text == "":
                    continue
                texts.append(text)
        # 改行部分は<SP>にしてflat にする
        output_files.append(" ".join(texts))        
        """
            for text in texts:
                if not text.strip():
                    continue
                if text:
                    text = texts[2:]
        # 配列なのであってもよいし、このチェックは必要ない
        if text not in output_files:
            output_files.append(text)
        """
    return output_files

# 関数は最初にかく
files = glob.glob('kaden-channel/*')
fs = map_lines(files)

with open("output.txt", 'w') as fd:
    for f in fs :
        fd.write("%s\n" % f)
