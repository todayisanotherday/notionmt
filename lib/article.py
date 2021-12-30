# coding: utf-8

import logging


class Article():

    def __init__(self, filename=""):
        self.filename = filename
        self.raw_doc = []

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
        with open(self.filename) as f:
            lines = f.readlines()
        self.raw_lines = lines
        logging.info("読み込み成功しました。")


    def parse(self):
        """ ファイルから記事ごとに解析する
        """
        MULTILINE = '-----\n'
        SPLITLINE = '--------\n'
        for line in self.raw_lines:
            if line == SPLITLINE:
                return
            elif line == MULTILINE:
                print
            else:
                print(line)
