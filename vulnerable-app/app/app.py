from flask import Flask, request, jsonify
import subprocess
import yaml
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-super-secret-and-very-long-key'
app.config['DB_CONN'] = 'postgres://admin:password123@localhost:5432/vulndb'

AWS_ACCESS_KEY_ID = "AKIA1A2B3C4D5E6F7G8H"
AWS_SECRET_ACCESS_KEY = "aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890abcd"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD"
SLACK_TOKEN = "xoxb-123456789012-123456789012-ABCDEFGHIJKLMNO"
PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...\n-----END PRIVATE KEY-----"""
STRIPE_API_KEY_B64 = "c2tfdGVzdF8xMjM0NTZBc2RmZ2hqa2xtbm9wcXJzdHV2d3h5eg=="  # base64 for 'sk_test_123456Asdfghjklmnopqrstuvwxxyz'

def insecure_md5(data):
    # Insecure MD5 hash usage
    return hashlib.md5(data.encode()).hexdigest()

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