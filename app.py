from flask import Flask, render_template, request, session, make_response
from articles import Article

app = Flask(__name__)
app.secret_key = 'thisisverysecret'
# Authentication & Authorization
# AuthN & AuthZ

articles = Article.all()

@app.route('/')
def home():
  return render_template("blog.html",articles=articles)

@app.route('/set-session')
def set_session():
  session['user_id'] = 1
  return 'session_set'

@app.route('/get-session')
def get_session():
  return f"user_id = {session['user_id']}"

@app.route('/first-time')
def first_time():
  if 'seen' not in request.cookies:
    response = make_response('you are new here')
    response.set_cookie('seen','1')
    return response
  seen = int(request.cookies['seen'])
  response = make_response(f'I have seen you before {seen} times')
  response.set_cookie('seen',str(seen+1))
  return response

@app.route("/blog/<slug>")
def article(slug:str):
  article = articles[slug]
  return render_template("article.html",title=article.title,content=article.content)

if __name__ == '__main__':
  app.run(port=4200,debug=True)