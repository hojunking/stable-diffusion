from googletrans import Translator
#pip install googletrans==3.1.0a0
#3.1.0a0를 설치해야 오류가 나지 않음

def translate(input):
    translator = Translator()
    translate = translator.translate(input)
    translate = str(translate)
    translate = translate.split(sep=',', maxsplit=3)
    output = translate[2][6:]
    return output