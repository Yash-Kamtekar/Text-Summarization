from elasticsearch import Elasticsearch
from mongoengine import connect, disconnect
from database_records import NewsArticle


def store_data_elastic(es):
    # CONNECTING TO MONGODB
    connect(
        db="cnbc",
        username="dataminingadmin",
        password="fall2021project",
        host="mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc",
    )

    # COLLECT ALL ARTICLES
    i = 0
    for article in NewsArticle.objects():
        es.index(
            index="mongo_db",
            doc_type="_doc",
            id=i,
            body={
                "source_name": article.source_name,
                "article_title": article.article_title,
                "article_authors": article.article_authors,
                "article_published_date": article.article_published_date,
                "article_text": article.article_text,
                "images_link": article.images_link,
                "video_link": article.video_link,
                "article_summary": article.article_summary,
                "article_keywords": article.article_keywords,
                "article_url": article.article_url,
            },
        )
        i += 1

    disconnect()


def connect_elasticsearch():
    es = Elasticsearch("https://localhost", port=9200)
    es = Elasticsearch()
    return es


def index_check(es, index):
    # CREATING AN INDICE
    if es.indices.exists(index=index):
        return "Index already present"
    else:
        print(es.indices.create(index=index))


def search_doc(es, body):
    return es.search(index="mongo_db", body=body)


body = {
    "size": 5,
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "article_text": {
                            "query": "california",
                            "prefix_length": 3,
                            "fuzziness": "3",
                            "operator": "and",
                        }
                    }
                }
            ]
        }
    },
}
