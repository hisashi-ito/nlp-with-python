#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#【wakachi】
#
# usage: wakachi.py -i <input> -o <output>
#
import sys
import argparse
import MeCab

# python3.5 から導入された型宣言を利用
# しかしあまり使っている人は見たことない。(これまでOSSで１回だけ見た)
from typing import List  
from pathlib import Path

class Main:
    
    def __init__(self, load_path, save_path):
        self.load_path = load_path
        self.save_path = save_path
        # インスタンス変数は事前に初期化しておくのがよいと思う
        # メソッドでいきなり定義して利用しても文法的にはOKであるが...
        self.texts = []        
        self.results = []
        
    def load_text(self) -> List[str]:
        with open(self.load_path, "r") as f:
            for line in f:
                # インスタンス変数に保存する
                self.texts.append(line.rstrip("\n"))
                
    def wakati_gaki(self) -> List[List[str]]:
        wakati = MeCab.Tagger("-Owakati")
        for x in self.texts:
            result = wakati.parse(x).split()
            print(result)
            self.results.append(result)
        # インスタンス変数に保存するならreturn しなくていい
        # return self.results

    def save_text(self):
        content = ""
        for x in self.results:
            content += " ".join(x) + "\n"

        # 最終行も改行があってもよい
        # content = content.rstrip("\n")
        with open(self.save_path, "w") as f:
            f.write(content)


if __name__ == "__main__":
    # argparse のインスタンスを作成
    parser = argparse.ArgumentParser()
    # 引数(-i)を設定
    parser.add_argument("-i", required=True, help='conf file')
    # 引数(-o)を設定
    parser.add_argument("-o", required=True, help='output file')
    # 設定した引数をparseする
    args = parser.parse_args()

    ins = Main(args.i, args.o)
    ins.load_text()
    ins.wakati_gaki()
    ins.save_text()
