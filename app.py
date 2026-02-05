from flask import Flask, render_template, make_response
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Flask looks in the /templates folder by default
    # This creates a response object so we can manually set the content type
    response = make_response(render_template('game.html'))
    response.headers['Content-Type'] = 'text/html'
    return response


if __name__ == '__main__':
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
