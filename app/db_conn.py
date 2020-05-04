import pandas as pd
from app import db
from app.models import Article, Category, Classification
from datetime import datetime


def import_excel(file_path):
    print("Importing scrape results from excel")
    df = pd.read_excel(
        file_path, "Sheet1", header=None,
        names=["URL", "Publisher", "DateTime", "Source", "Title", "Content"])
    df = df.fillna("")
    new_articles = list()
    for index, row in df.iterrows():
        if not Article.query.filter_by(url=row["URL"]).first():
            # This URL has not been scraped before
            article = Article(
                title=row["Title"],
                publisher=row["Publisher"],
                date=datetime.strptime(row["DateTime"], "%d %B %Y %I:%M%p"),
                url=row["URL"],
                content=row["Content"],
                sentiment=0,
                sentiment_magnitude=0
            )
            new_articles.append(article)
            db.session.add(article)
    db.session.commit()

    return new_articles


# def clear_data():
#     meta = db.metadata
#     for table in reversed(meta.sorted_tables):
#         print(f"Clear table {table}")
#         db.session.execute(table.delete())
#     db.session.commit()


def update_classifications(categories):
    for category in categories.keys():
        if not Category.query.filter_by(category=category).first():
            new_cat = Category(category=category)
            db.session.add(new_cat)
    db.session.commit()

    for category in categories:
        for article_id, confidence in categories[category]:
            cat = Category.query.filter_by(category=category).first()
            article = Article.query.filter_by(id=article_id).first()
            cls = Classification(confidence=confidence)
            cls.article = article
            cls.category = cat
            cat.articles.append(cls)
            article.categories.append(cls)
            db.session.add(article)
            db.session.add(cat)
            db.session.add(cls)
    db.session.commit()
    print("Database updated")


def update_sentiments(data):
    for record in data:
        article_id = record[0]
        score = record[1]
        magnitude = record[2]
        article = Article.query.filter_by(id=article_id).first()
        article.sentiment = score
        article.sentiment_magnitude = magnitude
        db.session.add(article)
    db.session.commit()
