from articles import Article

def test_article_init():
  a = Article('Test title')
  assert a.title == 'Test title'
  assert a.content == ''

def test_article_slug():
  a = Article('Test title')
  assert a.slug == 'test-title'