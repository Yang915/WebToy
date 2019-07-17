import os
from flask import Flask, render_template, request

from BP_get_answer import app_get_answer  # 返回应答语音的蓝图模块

app = Flask(__name__)
app.debug = True

app.register_blueprint(app_get_answer)  # 注册蓝图


@app.route('/ai_uploader', methods=['GET', 'POST'])
def answer():
    # 接收前端发来的语音消息，并指定路径保存
    reco_file = request.files.get('reco')
    # 调用uuid三方模块生成唯一文件名
    from uuid import uuid4
    filename = f'{uuid4()}.wav'

    filepath = os.path.join(os.path.dirname(__file__), 'audio', 'questions', filename)
    reco_file.save(filepath)
    # print('语音问题保存路径：',filepath)

    # 调用语音识别模块，对语音信息进行格式转换保存在指定目录，然后进行识别，得到文字信息
    from ASR import asr
    text_question = asr(filepath)
    # print('语音问题文本',text_question)

    # 调用自然语言处理模块，对文字信息进行处理，得到回复文字信息
    from NLP import nlp
    text_answer = nlp(text_question)
    # print('语音回答文本',text_answer)

    # 调用语音合成模块，对回复的文字信息进行合成并保存在指定目录下
    from TTS import tts
    answer_filepath = tts(text_answer)
    print('语音回答文件路径：', answer_filepath)

    # 获取语音应答消息文件名并返回
    answer_filename = os.path.basename(answer_filepath)
    return {'filename': answer_filename}


# 返回展示页面
@app.route('/record')
def get_record():
    return render_template('WebToy.html')


if __name__ == '__main__':
    app.run()
