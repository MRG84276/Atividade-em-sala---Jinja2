from flask import Flask,render_template,jsonify,request # type: ignore
import dados

app = Flask(__name__)
biblioteca = dados.carregar_do_arquivo()

@app.route('/html')
def heber():
     return jsonify(biblioteca)
    

@app.route("/biblioteca", methods=['GET','POST'])
@app.route('/biblioteca/<isbn>', methods=['GET', 'DELETE', 'PUT'])
def livro(isbn=None):
    return render_template("biblioteca.html", biblioteca=biblioteca)
    
@app.route('/biblioteca/criar', methods=['GET','POST'])
def criar_livro(): 
    if request.method == 'POST':
       novo_livro = {
            "isbn": request.form.get('isbn'),
             "ano_publicacao":request.form.get('ano_publicacao'),
             "autor": request.form.get('autor'),
             "editora": request.form.get('editora'),
             "genero": request.form.get('genero'),
             "localizacao": request.form.get('localizacao'),
             "paginas": request.form.get('paginas'),
             "status": request.form.get('status'),
             "titulo": request.form.get('titulo')
            }
       for l in biblioteca:
           if l['isbn'] == novo_livro['isbn']:
                return jsonify("Livro ja esta cadastrado"), 200
       biblioteca.append(novo_livro)
       dados.salvar_no_arquivo(biblioteca)
       return render_template('biblioteca.html', biblioteca=biblioteca)
    else:
       return render_template('criar_livro.html')
if __name__ == '__main__':
   app.run(debug=True)


