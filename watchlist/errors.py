#错误处理函数
from watchlist import app
from flask import render_template

################################################################错误处理函数#######################################################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'),404