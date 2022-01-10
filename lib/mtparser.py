# coding: utf-8

from lark import Lark, Transformer
from functools import reduce
import logging, pprint



class MTTransformer(Transformer):
    start = list

    def article(self, tokens):
        return tokens
    def metafields(self, tokens):
        return {'metafields' : reduce(lambda x,y: {**x, **y}, tokens)}
    def metafield(self, tokens):
        return { tokens[0].value : tokens[1].value }
    def sectionfields(self, tokens):
        return {'sectionfields' : reduce(lambda x,y: {**x, **y}, tokens)}
    def sectionfield(self, tokens):
        return { tokens[0].value : tokens[1] }
    def sectionvalue(self, tokens):
        return tokens[0]
    def sectionmetafields(self, tokens):
        return {'sectionmetafields' : reduce(lambda x,y: {**x, **y}, tokens)}
    def sectionmetafields(self, tokens):
        return tokens
    def textlines(self, tokens):
        return "".join(tokens)
    def textline(self, tokens):
        return tokens[0].value


class MTParser():
    """ MTParser
        MovableType形式のファイルを解析するクラス
    """

    GRAMMER_FILENAME = './lib/mtparser.lark'

    def __init__(self, text: str = []):
        """コンストラクタ

        Args
            textlines (str, optional): 解析対象文字列
        """
        self.text = text

    def parse(self):
        with open(self.GRAMMER_FILENAME, 'r') as fs:
            grammer = ''.join(fs.readlines())
        parser = Lark(grammer,
                    start='start',
                    parser='lalr',
                    transformer=MTTransformer(),
                    )
        result = parser.parse(self.text)
        logging.info(pprint.pformat(result))
