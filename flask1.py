from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def page1():
   return render_template("page1.html",no = 1)
@app.route('/page2/')
def page2():
   return render_template("page2.html",no = 2)

if __name__ == "__main__" :
    app.run(debug=True)




