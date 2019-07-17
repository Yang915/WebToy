import os
from aip import AipSpeech

APP_ID = '16815394'
API_KEY = 'jM4b8GIG9gzrzySTRq3szK2E'
SECRET_KEY = 'iE626cEpjT1iAVwh24XV5h1QFuR8FPD2'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



# 读取文件
def get_file_content(filepath):

    #文件格式转换成pcm(前提是需要安装ffmpeg软件并配置环境变量)
    filename=os.path.basename(filepath)
    pcm_filename = filename.split('.')[0] + '.pcm'
    pcm_filepath=os.path.join(os.path.dirname(__file__),'audio','pcm',pcm_filename)
    cmd_str=f'ffmpeg -y  -i {filepath}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {pcm_filepath}'#ffmpeg软件安装及环境变量配置
    os.system(cmd_str)#调用os.system()在CMD执行命令
    filepath=pcm_filepath

    with open(filepath, 'rb') as fp:
        return fp.read()


# 识别本地文件
def asr(filePath):
    pcm_file=get_file_content(filePath)
    result=client.asr(pcm_file, 'pcm', 16000, {
        'dev_pid': 1536,
    })
    print(result)
    try:
        text=result.get('result')[0]
    except:
        text='!@#$%^&^%$#$%^&*'
    # print(text)
    return text




