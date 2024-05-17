from flask import Flask, render_template
from controllers.api_controller import api_controller

app = Flask(__name__)
app.register_blueprint(api_controller)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
