from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required,  current_user
from models.product import Produto


produto_bp = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='views/produtos')

@produto_bp.route("/")
@login_required 
def produtos():
    produtos = Produto.all()
    return render_template("produtos/produtos.html", produtos=produtos)

@produto_bp.route("/adicionar", methods=["GET", "POST"])
@login_required 
def adicionar():
    if request.method == 'POST':
        produto = Produto(nome=request.form["nome"], preco=float(request.form["preco"]),
            descricao = request.form["descricao"],
            user_id= current_user.id)
        
        produto.save()
        flash("Produto adicionado com sucesso!", "success")
        return redirect(url_for("produtos.produtos"))
    return render_template('produtos/adicionar_produto.html')

@produto_bp.route("/remover/<int:item>", methods=["POST"])
@login_required 
def remover(item):
    p = Produto.get(item)
    if p: p.delete()
    flash("Produto removido!", "success")
    return redirect(url_for("produtos.produtos"))

@produto_bp.route("/editar/<int:item>", methods=["GET", "POST"])
@login_required 
def editar(item):
    p = Produto.get(item)
    if not p:
        flash("Produto não encontrado!", "error")
        return redirect(url_for("produtos.produtos"))

    if request.method == "POST":
        p.update(nome=request.form.get("nome"),preco=float(request.form.get("preco", 0)),descricao=request.form.get("descricao"))
        flash("Produto editado!", "success")
        return redirect(url_for("produtos.produtos"))

    return render_template('produtos/editar_produto.html', produto=p)