# coding: utf-8

import logging
import json
import argparse
from article import Article


def main():
    """メイン関数
    """

    # ログ設定
    logging.basicConfig(
        format=json.dumps({
            'level':  '%(levelname)s',
            'time':  '%(asctime)s',
            'message':  '%(message)s',
        }),
        level=logging.DEBUG,
    )

    # コマンドライン引数解析
    parser = argparse.ArgumentParser(description='''
    MovableType形式のファイルをnotionにインポートするプログラムです。
    ''')
    parser.add_argument('filename', type=str, help='読み込むファイル名')
    parser.add_argument('--dry', '-d', action='store_true', help='ファイル読込のみ実施')
    args = parser.parse_args()
    logging.debug(f'コマンドライン引数:{args}')

    # 解析
    try:
        article = Article(filename=args.filename)
        article.load()
        result = article.parse()
        with open('./result.txt', 'w') as f:
            f.write(result)
    except Exception as e:
        logging.error(e)
        logging.info('エラー終了')

    # notion出力


if __name__ == '__main__':
    main()
