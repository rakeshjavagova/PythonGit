from flask import Flask, jsonify

app = Flask(__name__)

# Sample data - you can replace this with your actual data source
books = [
    {"id": 1, "title": "Python Programming", "author": "John Smith"},
    {"id": 2, "title": "Java Basics", "author": "Jane Doe"},
    {"id": 3, "title": "Advance Java", "author": "Jane Doe"},
    {"id": 4, "title": "Advance Java", "author": "Jane Doe"},
    {"id": 5, "title": "Advance Java", "author": "Jane Doe"}
]

# Define a route for handling GET requests
#hello
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
