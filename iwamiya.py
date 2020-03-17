# -*- coding: utf-8 -*-
import fasttext as ft
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import MeCab
import re

# flaskの使い方
# https://medium.com/nyle-engineering-blog/flask%E3%81%A7rest-api%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%8B-fad8ae1fde5c
# curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"vision":"test1", "learn":"test2", "analyze":"test3"}' http://localhost:5000

def main():
    args = sys.argv
    
    if len(sys.argv) < 4:
        viewUsecase()

    app = Flask(__name__)
    CORS(app)
    app.config['JSON_AS_ASCII'] = False
    @app.route('/', methods=['POST'])
    def post_json():
        json = request.get_json(force=True)
        VISION = json['vision']
        LEARN = json['learn']
        ANALYZE = json['analyze']
        dic = {
            'vision': str(modelClassifier(args[1], VISION)),
            'learn': str(modelClassifier(args[2], LEARN)),
            'analyze': str(modelClassifier(args[3], ANALYZE))
        }
        return jsonify(dic)

    app.run(debug=True, host='0.0.0.0')

def modelClassifier(modelName, strs):
    mecab = MeCab.Tagger ("-Owakati")
    text = format_text(mecab.parse(strs))
    # print('model: ' + modelName + ' wakati: ' + text)
    return predict_language(text, modelName)

def predict_language(text, modelName):
    classifier = ft.load_model(modelName)
    label, prob = classifier.predict(text)
    return format_result(str(label)) + ":" + format_result(str(round(int(prob) * 100)))

def format_result(text):
    text=re.sub('\[', "", text)
    text=re.sub('\]', "", text)
    text=re.sub('\(', "", text)
    text=re.sub('\)', "", text)
    text=re.sub('\'', "", text)
    text=re.sub(',', "", text)
    text=re.sub('__label__', "", text)
    return text

def format_text(text):
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'&[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(';', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('\n', " ", text)
    return text

def viewUsecase():
    print("usecase: python iwamiya.py arg1:(vision model) arg2:(learn model) arg3:(analyze model) ")
    sys.exit()

if __name__ == '__main__':
    main()
