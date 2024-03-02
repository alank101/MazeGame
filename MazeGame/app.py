from flask import Flask, render_template, jsonify
from GameMap import maze

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/maze_data')
def get_maze_data():
    return jsonify(maze)

if __name__ == '__main__':
    app.run(debug=True)