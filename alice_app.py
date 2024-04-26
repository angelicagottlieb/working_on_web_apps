# import os 
# from flask import Flask, request # Remember to import `request`

# app = Flask(__name__)

# # Request:
# # POST /goodbye
# #   With body parameter: name=Alice

# @app.route('/goodbye', methods=['POST'])
# def goodbye():
#     name = request.form['name'] # The value is 'Alice'

#     # Send back a fond farewell with the name
#     return f"Goodbye {name}!"

# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
