from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Flask looks in the /templates folder by default
    # This creates a response object so we can manually set the content type
    return render_template('index.html')  # Flask handles the "text/html" header for you


if __name__ == '__main__':
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
