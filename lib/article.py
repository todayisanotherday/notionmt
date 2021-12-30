# coding: utf-8

import logging
from mtparser import MTParser

class Article():

    def __init__(self, filename=""):
        self.filename = filename
        self.raw_lines = []

    def load(self) -> list[str]:
        """ ファイル読み取り
        Args:
            filename (str): ファイル名

        Returns:
            list(str): ファイル全文
        """
        logging.info(f'読み込むファイル名:{self.filename}')
        if not self.filename:
            logging.warning("ファイル名がセットされていません。")
            return
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.raw_lines = lines
        logging.info("読み込み成功しました。")


    def parse(self):
        """ ファイルから記事ごとに解析する
        """
        logging.info("解析開始します。")
        parser = MTParser(self.raw_lines)
        parser.parse()