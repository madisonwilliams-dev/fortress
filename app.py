from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Flask looks in the /templates folder by default
    return render_template('game.html')

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
