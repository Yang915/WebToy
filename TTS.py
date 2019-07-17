import os

from aip import AipSpeech

APP_ID = '16815394'
API_KEY = 'jM4b8GIG9gzrzySTRq3szK2E'
SECRET_KEY = 'iE626cEpjT1iAVwh24XV5h1QFuR8FPD2'

SPEECH_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


#TTS合成语音文件（语音合成）
VOICE={'spd':5,'pit':7,'vol': 6,'per':4,}


def tts(text_answer):

    audio=SPEECH_client.synthesis(text_answer,'zh',1,VOICE)
    from uuid import uuid4
    answer_filepanme = f'{uuid4()}.mp3'
    answer_filepath = os.path.join(os.path.dirname(__file__), 'audio', 'answers', answer_filepanme)

    if not isinstance(audio,dict):
        with open(answer_filepath,'wb') as f:
            f.write(audio)

    return answer_filepath