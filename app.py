from flask import Flask, render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    # Run the Flask app with host set to '0.0.0.0' to listen on all network interfaces
    app.run(host='0.0.0.0', debug=True)
    