from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Route for dynamic user profile pages
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the app with custom port and debugging enabled
if __name__ == '__main__':
    app.run(port=5555, debug=True)
