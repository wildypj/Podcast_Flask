from flask import Flask, render_template, request, send_from_directory
from api_communication import save_transcript
from werkzeug.exceptions import abort
from flask_caching import Cache
import json


app = Flask(__name__)

# Add cache configuration
cache = Cache()
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)

@app.route('/')
def index():
    sample_data = {} 
    return render_template('index.html', data=sample_data)

@app.route('/summary/<episode_id>')
@cache.cached(timeout=3600)  # Cache for 1 hour
def fetch_summary(episode_id):
    print("Fetching summary for episode ID:", episode_id)  # Debug print
    success = save_transcript(episode_id)
    if success:
        filename = f"{episode_id}_chapters.json"
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    else:
        return json.dumps({"error": f"Failed to save transcript for episode ID {episode_id}. Please try again."})

@app.route('/transcripts/<path:filename>')
def serve_transcript(filename):
    return send_from_directory(directory='', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

