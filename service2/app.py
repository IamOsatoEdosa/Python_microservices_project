from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': [{'book_id': 1, 'review': 'Great Book!'}]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
