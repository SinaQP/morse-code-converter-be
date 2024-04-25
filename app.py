from flask import Flask, request, jsonify
from morseConverter import MorseConverter

converter = MorseConverter()

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def main():
    return "Morse Code Converter"


@app.route(r'/encode', methods=['POST'])
def encode():
    """Encodes an English message into Morse code via a POST request."""

    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'Missing required field "message"'}), 400

    morse_code = converter.encode(message)
    return jsonify({'morse_code': morse_code})


@app.route(r'/decode', methods=['POST'])
def decode():
    """Decodes Morse code into an English message via a POST request."""

    morse_code = request.json.get('morse_code')
    if not morse_code:
        return jsonify({'error': 'Missing required field "morse_code"'}), 400
    english_message = converter.decode(morse_code)
    return jsonify({'message': english_message})


if __name__ == '__main__':
    app.run(debug=True)
