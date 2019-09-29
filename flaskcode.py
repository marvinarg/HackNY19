from flask import Flask, request, render_template
app = Flask(__name__)

#@app.route('/')
#@app.route('/index', methods=["GET", "POST"])
#def index():
    #if request.method == "POST":
        #print("posted to /user")
        #print(request.form)
        #data = request.form['fname']
        #return str(data)


@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)