from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/profile/')
@app.route('/profile/<name>')
def profile(name=None):
    context = {
        'name': name,
    }
    return render_template('profile.html', context=context)



if __name__=="__main__":
    app.run(debug=True)