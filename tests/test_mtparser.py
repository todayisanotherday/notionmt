from lib.mtparser import MTParser

def test_create_object():
  parser = MTParser()
  assert parser is not None

def test_parse_text_success():
  text = '''AUTHOR: sample
TITLE: タイトル
BASENAME: 2021/12/31/010837
STATUS: Publish
ALLOW COMMENTS: 0
CONVERT BREAKS: 0
DATE: 12/31/2021 01:08:37
-----
BODY:
<p>ああああああああああああああああああああ</p>
<p>ああああああああああああああああああああ</p>
-----
--------
AUTHOR: sample
TITLE: アアアアアアア
BASENAME: 2021/12/30/000836
STATUS: Publish
ALLOW COMMENTS: 0
CONVERT BREAKS: 0
DATE: 12/30/2021 00:08:36
CATEGORY: 日記
-----
BODY:
<p>ああああああああああああああああああああ</p>
<p>ああああああああああああああああああああ</p>
-----
--------
'''
  parser = MTParser(textlines=text)
  result = parser.parse()
  assert True