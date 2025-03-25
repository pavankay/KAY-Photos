from flask import Flask, render_template, send_file, Response, send_from_directory
import os

app = Flask(__name__)

def get_content_type(filename):
    if filename.endswith('.js.br'):
        return 'application/javascript'
    elif filename.endswith('.wasm.br'):
        return 'application/wasm'
    elif filename.endswith('.data.br'):
        return 'application/octet-stream'
    return 'application/octet-stream'

@app.route("/")
def home():
    return '<a href="/photos">Photos</a> | <a href="/game">Game</a>'

@app.route("/photos")
def photos():
    return render_template('index.html')

@app.route("/game")
def game():
    return send_file('AJGame/game.html')

@app.route('/game/<path:filename>')
def serve_game_file(filename):
    file_path = os.path.join(os.getcwd(), 'AJGame', filename)
    
    if not os.path.exists(file_path):
        return "File not found", 404
    
    # Handle .br files with proper headers
    if filename.endswith('.br'):
        with open(file_path, 'rb') as f:
            content = f.read()
        return Response(
            content,
            mimetype=get_content_type(filename),
            headers={'Content-Encoding': 'br'}
        )
    
    # For files in subdirectories
    directory = os.path.join(os.getcwd(), 'AJGame')
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run(debug=True)