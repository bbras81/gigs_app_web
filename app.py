from flask import Flask, render_template, redirect, url_for, flash, request
from forms import EmpresaForm
import db

db.main()
app = Flask(__name__)

app.secret_key = 'ervqepvjnepivjneqpivejnpijnqepijvnqepivjnqepijvnqepijvmnepojv'

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add_client', methods=['GET', 'POST'])
def add_clients():
    form = EmpresaForm()
    if form.validate_on_submit():
        # Processar os dados do formulário
        nome_empresa = form.nome_empresa.data
        nif = form.nif.data
        endereco = form.endereco.data
        codigo_postal = form.codigo_postal.data
        localidade = form.localidade.data
        email = form.email.data
        telefone = form.telefone.data
        website = form.website.data
        
        db.db_execute("INSERT INTO clients (nome_empresa, nif, morada, cp, localidade, email, telefone) VALUES (?, ?, ?, ?, ?, ?, ?) ",
                      [nome_empresa,
                      nif,
                      endereco,
                      codigo_postal,
                      localidade,
                      email,
                      telefone]
                      )

        flash('Empresa registada com sucesso!', 'success')
        return redirect("/")
    return render_template('clients.html', form=form)




@app.route('/view_client', methods=['GET', 'POST'])
def view_client():
        client_id_get = 1
        client_view = db.db_execute("SELECT * FROM clients WHERE id_cliente = ?", (client_id_get,), fetch_one=True)
        return render_template('client_view.html', client=client_view)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
