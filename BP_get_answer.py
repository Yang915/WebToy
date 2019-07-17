import os
from flask import Blueprint, send_file, request

dir_static = os.path.join('audio', 'answers')
app_get_answer = Blueprint('get_answer', __name__,static_folder=dir_static, static_url_path='/get_answer')


@app_get_answer.route('/<filename>')
def get_answer(filename):

    return send_file(filename)
