from flask import Flask, request, jsonify

app = Flask(__name__)

def execute(numbers):
    result = sum(numbers)
    return {"result": result}

@app.route('/process', methods=['POST'])
def process():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        numbers = []
        for line in file.readlines():
            line = line.strip()
            if line.isdigit():
                numbers.append(int(line))
            else:
                return jsonify({"error": f"Invalid number format: {line}"}), 400

        response = execute(numbers)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

