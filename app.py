import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods=['POST'])
def submit_hello_world():
    name = request.form['name']
    message = request.form['message']
    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels_eunoia():
    text = request.form['text']
    vowel_number = 0
    vowels = "aeiou"
    for letter in text:
        if letter.lower() in vowels:
            vowel_number = vowel_number + 1
    return f"There are {vowel_number} vowels in \"{text}\""

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    names = request.form['names']
    list_of_names_split = names.split(',')
    list_of_names = list(list_of_names_split)
    sorted_names = sorted(list_of_names)
    return ','.join(sorted_names)

@app.route('/names', methods=['GET'])
def names_plus_new_name():
    predefined_list = ["Julia", "Alice", "Karim"]
    added = request.args['add']
    predefined_list.append(added)
    return ', '.join(predefined_list)



# == Example Code Below ==

# # GET /emoji
# # Returns a emojiy face
# # Try it:
# #   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

from music_web_app import apply_example_music_app
apply_example_music_app(app)


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

