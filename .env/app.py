from flask import Flask,render_template
app=Flask(__name__)
# @app.route('/')
# def hello():
#     return '<h1>Hello Welcome!</h1><img src="https://ts1.cn.mm.bing.net/th/id/R-C.a993c3e3e1190b7ffe64d19d740b4ebc?rik=J8%2fVBdAfU7aWmw&riu=http%3a%2f%2fpic.baike.soso.com%2fp%2f20131206%2f20131206131902-927067888.jpg&ehk=Va3qMSkZSF3pgSsxtrzumpkXsgZdKaf447GQ6kqhvxo%3d&risl=&pid=ImgRaw&r=0">'
name = 'Hxhdhcjmet'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)