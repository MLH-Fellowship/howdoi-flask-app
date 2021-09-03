# this runs in the start when app.run is called since the constructor


# -----> trivial file sections
from app.howdoi_logic.search_with_howdoi import send_output
from flask import Flask, jsonify, render_template, send_file, make_response
from flask_restful import Api, reqparse
from app.utils.helpers import api_response
from app.utils.search import get_output
import json

# ------> 
# creating an instance of flask 
app = Flask(__name__)
# api calling utility
api = Api(app)


def search_which_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('query')
    return parser

# if it is the home route
@app.route('/')
def home():
    # get your parser from function at line 18
    parser = search_which_parser()
    tokens = parser.parse_args()
    #  if howdpi runs fine and works perfectly 
    if tokens.get('query'):
        output = send_output(tokens['query'])
        # now come the headers
        # howdoi uses text and html fils for answer rendering 
        headers = {'Content-Type': 'text/html'}
        with open('./data.json' 'r+') as my_data:
            # getting the data inside file
            my_object = json.load(my_data)
            # count stores thenumber of times howdoi flask was used for searching
            count = my_object['count']
            count+=1
            # reqrite the data back into the file
            my_object['count'] = count
            my_data.seek(0)
            my_data.truncate
            json.dump(my_object, my_data, indent = 4)
            my_data.close()
            # make response with code 200=> ok
        return make_response(render_template('result.html', output=str(output), query=str(tokens['query'])), 200, headers)
    # if howdoi doesnt give ans
    else:
    # still update the count 
        with open('./datanjson' , 'r+') as my_data:
            my_object = json.load(my_data)
            count = my_object['count']
            my_data.close()
            # return the home page itself but with changes count 
        return render_template('home.html', count=count)
