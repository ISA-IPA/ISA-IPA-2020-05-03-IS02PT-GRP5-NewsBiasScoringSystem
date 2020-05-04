from app import db

phrase_associations = db.Table(
    "Topic Association",
    db.Column("topic_id", db.Integer, db.ForeignKey("topic.id")),
    db.Column("article_id", db.Integer, db.ForeignKey("article.id"))
)


class Classification(db.Model):
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"),
                           primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"),
                            primary_key=True)
    confidence = db.Column(db.Float)
    article = db.relationship("Article", back_populates="categories")
    category = db.relationship("Category", back_populates="articles")


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    publisher = db.Column(db.String(50), index=True)
    date = db.Column(db.DateTime, index=True)
    url = db.Column(db.String(200), unique=True)
    content = db.Column(db.String(5000))
    sentiment = db.Column(db.Float)
    sentiment_magnitude = db.Column(db.Float)

    categories = db.relationship("Classification", back_populates="article")

    phrases = db.relationship("Topic", secondary=phrase_associations,
                              backref="articles")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), index=True, unique=True)

    articles = db.relationship("Classification", back_populates="category")


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(100), index=True, unique=True)
