from flask import Flask,render_template,jsonify  # type: ignore
import dados

app = Flask(__name__)
biblioteca = dados.carregar_do_arquivo()

@app.route('/html')
def heber():
    return render_template("biblioteca.html", biblioteca=biblioteca)
    

@app.route("/biblioteca", methods=['GET','POST'])
@app.route('/biblioteca/<isbn>', methods=['GET', 'DELETE', 'PUT'])
def livro(isbn=None):
     return jsonify(biblioteca)

if __name__ == '__main__':
   app.run(debug=True)


