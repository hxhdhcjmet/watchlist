from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return '<h1>Hello Welcome!</h1><img src="https://ts1.cn.mm.bing.net/th/id/R-C.a993c3e3e1190b7ffe64d19d740b4ebc?rik=J8%2fVBdAfU7aWmw&riu=http%3a%2f%2fpic.baike.soso.com%2fp%2f20131206%2f20131206131902-927067888.jpg&ehk=Va3qMSkZSF3pgSsxtrzumpkXsgZdKaf447GQ6kqhvxo%3d&risl=&pid=ImgRaw&r=0">'