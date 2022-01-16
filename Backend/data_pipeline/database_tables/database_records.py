from mongoengine import Document, StringField, URLField, ListField


class NewsArticle(Document):
    source_name = StringField(required=True)
    article_title = StringField(required=True)
    article_authors = ListField()
    article_published_date = StringField()
    article_text = StringField(required=True)
    images_link = StringField()
    video_link = ListField()
    article_summary = StringField(required=True)
    article_keywords = ListField()
    article_url = URLField(required=True)
    meta = {'allow_inheritance': True}
