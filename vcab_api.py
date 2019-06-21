
from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
from flask_restful import Resource, Api
api = Api(app)
CORS(app)
from flask import request
import spell_corrector

class Vocab_Correct(Resource):
    def get(self):

        word = request.args.get('query')
        print(word)
        ans = spell_corrector.spell_check(str(word))
        print(ans)
        ans_json = {
            "Correct Vocab Predictions: " : ans
        }
        return ans_json


api.add_resource(Vocab_Correct, '/CorrectVocab')  # Translate Route


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)