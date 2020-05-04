from app import app, db
from flask import render_template, request
from .models import Article, Category, Classification
# from .forms import FilterForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_cats = request.form.getlist("category")
        if len(selected_cats) == 0:
            articles = Article.query.all()
        else:
            classifications = Classification.query.filter(
                Classification.category_id.in_(selected_cats)).all()
            cls_ids = [cls.article_id for cls in classifications]
            articles = Article.query.filter(Article.id.in_(cls_ids)).all()
    else:
        articles = Article.query.all()

    cat_filters = [(cat.id, cat.category) for cat
                   in Category.query.order_by(Category.category).all()]
    return render_template("index.html", title="Home", articles=articles,
                           cat_filters=cat_filters)
