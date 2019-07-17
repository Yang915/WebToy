from aip import AipNlp
from TuringRobotAPI import turingRobotAnswer

APP_ID = '16815394'
API_KEY = 'jM4b8GIG9gzrzySTRq3szK2E'
SECRET_KEY = 'iE626cEpjT1iAVwh24XV5h1QFuR8FPD2'

NLP_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)



def nlp(text_question):
    text_answer='我是无所不知的智能小机器人飞飞！'
    score=NLP_client.simnet(text_question,'你叫什么名字').get('score')
    if score < 0.58 :
        text_answer=turingRobotAnswer(text_question)
    return text_answer
