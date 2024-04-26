# import os
# from flask import Flask, request

# app = Flask(__name__)

# # Request:
# # GET /hello?name=David

# @app.route('/hello', methods=['GET'])
# def hello():
#     name = request.args['name'] # The value is 'David'

#     # Send back a friendly greeting with the name
#     return f"Hello {name}!"

# # To make a request, run:
# # curl "http://localhost:5000/hello?name=David"
# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
