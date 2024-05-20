from flask import Flask, render_template

app=Flask(__name__)
    
@app.route("/")
def principal():
 return render_template("base.html")

@app.route("/contacto")
def contacto():
 return render_template("contacto.html")

@app.route("/galeria")
def galeria():
 return render_template("galeria.html")

if __name__ == 	'__main__':
    app.run(debug=True,port=3500)