from flask import Flask,jsonify,request,render_template,abort
from methods import search_by_id, search_by_title, search_by_year, recommendation


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

file = open('data.tsv', encoding='utf-8')
data = file.readlines()
file.close()


@app.route('/')
def home():
    return '<h1>Hello</h1>'

@app.route('/movie_id/<string:movie_id>', methods = ['GET'])
def get_movie_by_id(movie_id):
    answer = search_by_id(movie_id, data)
    if (answer):
        return jsonify(answer)
    else:
        abort(404) 

@app.route('/movie/<string:title>', methods = ['GET'])
def get_movies_by_title(title):
    answer = search_by_title(title, data)
    if(len(answer) == 0):
        abort(404)
    
    return jsonify(answer)

@app.route('/year/<int:year>', methods = ['GET'])
def get_movie_by_year(year):
    answer = search_by_year(year, data)
    if(len(answer) == 0):
        abort(404)

    return jsonify(answer)

@app.route('/suggest/<int:topk>', methods = ['POST'])
def suggest(topk):
    if (topk >= len(data) and topk <= 0):
        abort(404)

    answer = recommendation(topk, request.get_json(), data)
    sorted_list = dict(sorted(answer.items(), key = lambda item: item[1], reverse=True))

    return jsonify({'ratings': sorted_list})    


app.run(debug=True, host='0.0.0.0')
