from google.cloud import language
from app.db_conn import update_classifications, update_sentiments


def classify(text):
    language_client = language.LanguageServiceClient()
    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(document)
    categories = response.categories
    result = {}
    for category in categories:
        result[category.name] = category.confidence

    return result


def classify_articles(articles):
    print(f"Classifying {len(articles)} articles using Google NLP")
    categories = dict()
    for article in articles:
        classifications = classify(article.content)
        for classification, confidence in classifications.items():
            if confidence >= 0.5:
                if classification not in categories.keys():
                    categories[classification] = [(article.id, confidence)]
                else:
                    categories[classification].append((article.id, confidence))

    update_classifications(categories)


def analyse_sentiment(text):
    language_client = language.LanguageServiceClient()
    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT
    )
    sentiment = language_client.analyze_sentiment(document)
    score = sentiment.document_sentiment.score
    magnitude = sentiment.document_sentiment.magnitude

    return score, magnitude


def analyse_article_sentiments(articles):
    print(f"Analysing sentiments for {len(articles)} articles using Google "
          f"NLP")
    results = list()
    for article in articles:
        score, magnitude = analyse_sentiment(article.content)
        results.append((article.id, score, magnitude))

    update_sentiments(results)