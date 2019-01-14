import csv

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():

    # Get html and render to screen
    index_file = open('index.html', 'r')
    index_html = index_file.read()
    # index_html = index_html.replace('{{blog_posts}}', blog_post_html)
    index_file.close()

    return index_html
