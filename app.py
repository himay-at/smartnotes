from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')

    # Dummy GPT-like reply
    response = f"🤖 GPT says: You asked — '{question}'"

    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)