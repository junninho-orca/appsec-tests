from flask import Flask, request, jsonify
import subprocess
import yaml

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-super-secret-and-very-long-key'
app.config['DB_CONN'] = 'postgres://admin:password123@localhost:5432/vulndb'

@app.route('/')
def index():
    return 'Welcome to the intentionally vulnerable app!'

@app.route('/execute')
def execute():
    cmd = request.args.get('command')
    if not cmd:
        return 'No command provided', 400
    # Command injection vulnerability
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return jsonify({
        'command': cmd,
        'output': result.stdout,
        'error': result.stderr
    })

@app.route('/load_yaml', methods=['POST'])
def load_yaml():
    data = request.data.decode('utf-8')
    # Unsafe yaml.load usage
    loaded = yaml.load(data)
    return jsonify({'loaded': str(loaded)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 