from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    response = requests.get('http://reviewservice:5002/reviews')
    reviews = response.json()
    return jsonify({'books': [{'id': 1, 'title': 'Book One', 'reviews': reviews}]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
