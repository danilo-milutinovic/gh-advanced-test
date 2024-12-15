from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    user_input = request.args.get('name', '')  # Vulnerable: unsanitized input
    template = f"<h1>Hello, {user_input}</h1>"  # Potential XSS
    return render_template_string(template)

@app.route('/file')
def read_file():
    filename = request.args.get('filename', '')  # Vulnerable: unsanitized input
    try:
        with open(filename, 'r') as f:  # Vulnerable: path traversal
            return f.read()
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)
