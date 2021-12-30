# coding: utf-8

from enum import Enum
import logging


class MTMode(Enum):
    """ 解析時の状態を定義
    """
    SINGLE_LINE = 'SINGLE_LINE'  # 単体行情報
    MULTI_LINE = 'MULTI_LINE'  # 複数行情報


class MTParser():
    """ MTParser
      MovableType形式のファイルを解析するクラス
      再帰下降構文解析による実装を目指す
    """

    SPLITLINE = '--------\n'  # 区切り線
    MULTILINE = '-----\n'  # 複数行

    def __init__(self, textlines: list[str] = []):
        """コンストラクタ

        Args
            textlines (list[str], optional): fs.readlinesで取得した解析対象. Defaults to [].
        """
        self.textlines = textlines

    def parse(self, mode=MTMode.SINGLE_LINE):
      pass