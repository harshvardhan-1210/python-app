from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python app on Elastic Beanstalk!"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # For demo purposes, no authentication logic; just echo back
        return jsonify({"message": f"Login attempt for {username}"})
    return render_template('login.html')

@app.route('/health')
def health():
    return jsonify({"status": "OK", "environment": os.environ.get('FLASK_ENV', 'development')}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_ENV') == 'development')