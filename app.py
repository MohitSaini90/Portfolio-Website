from flask import Flask, render_template
from waitress import serve
app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')
# Use mode='dev' for Flask in development mode and mode='prod' for flask in production mode
mode="prod" 
if __name__ == "__main__":
    if mode=="dev":
        app.run(host='0.0.0.0' , port=50100, debug=True)
    else:
        serve(app, host='127.0.0.1', port=5000, threads=1)

