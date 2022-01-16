import logging
import pandas as pd
from mongoengine import connect, disconnect
from Backend.data_pipeline.database_tables.database_records import NewsArticle
from news_articles import parse_article
from tqdm import tqdm
import glob
import time

# initializing the logger
logging.basicConfig(filename='../Logs/news_articles.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


def add_records_to_newyork_database(file_name):
    connect(db='newyorktimes',
            username='dataminingadmin',
            password='fall2021project',
            host='mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')

    newyork_times_file = pd.read_excel(file_name, engine='openpyxl')

    for index, row in tqdm(newyork_times_file.iterrows(), total=newyork_times_file.shape[0]):
        try:
            article_data = parse_article(row['Article_Link'])
            current_article = NewsArticle()
            current_article.source_name = "Newyork Times"
            current_article.article_title = article_data['article_title']
            current_article.article_authors = article_data['article_authors']
            if len(article_data['article_published_date']) == 0:
                current_article.article_published_date = row['Date']
            else:
                current_article.article_published_date = article_data['article_published_date']
            current_article.article_text = article_data['article_text']
            current_article.images_link = article_data['images_link']
            current_article.video_link = article_data['video_link']
            current_article.article_summary = article_data['article_summary']
            current_article.article_keywords = article_data['article_keywords']
            current_article.article_url = article_data['article_url']

            current_article.save()
        except Exception as e:
            logging.error('Failed for article link-' + str(row['Article_Link']))
            logging.error(e)
            print(e)

    disconnect()


def add_records_to_cnbc_database(file_name):
    connect(db='cnbc',
            username='dataminingadmin',
            password='fall2021project',
            host='mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc')

    cnbc_files = pd.read_excel(file_name, engine='openpyxl')

    for index, row in tqdm(cnbc_files.iterrows(), total=cnbc_files.shape[0]):
        try:
            article_data = parse_article(row['Article_Link'])
            current_article = NewsArticle()
            current_article.source_name = "CNBC"
            current_article.article_title = article_data['article_title']
            current_article.article_authors = article_data['article_authors']
            if len(article_data['article_published_date']) == 0:
                current_article.article_published_date = row['Date']
            else:
                current_article.article_published_date = article_data['article_published_date']
            current_article.article_text = article_data['article_text']
            current_article.images_link = article_data['images_link']
            current_article.video_link = article_data['video_link']
            current_article.article_summary = article_data['article_summary']
            current_article.article_keywords = article_data['article_keywords']
            current_article.article_url = article_data['article_url']

            current_article.save()
        except Exception as e:
            logging.error('Failed for article link-' + str(row['Article_Link']))
            logging.error(e)
            print(e)

    disconnect()


def add_records_to_latimes_database(file_name):
    connect(db='latimes',
            username='dataminingadmin',
            password='fall2021project',
            host='mongodb+srv://dataminingadmin:fall2021project@cluster2.ngjps.mongodb.net/latimes')

    cnbc_files = pd.read_excel(file_name, engine='openpyxl')

    for index, row in tqdm(cnbc_files.iterrows(), total=cnbc_files.shape[0]):
        try:
            article_data = parse_article(row['Article_Link'])
            current_article = NewsArticle()
            current_article.source_name = "latimes"
            current_article.article_title = article_data['article_title']
            current_article.article_authors = article_data['article_authors']
            if len(article_data['article_published_date']) == 0:
                current_article.article_published_date = row['Date']
            else:
                current_article.article_published_date = article_data['article_published_date']
            current_article.article_text = article_data['article_text']
            current_article.images_link = article_data['images_link']
            current_article.video_link = article_data['video_link']
            current_article.article_summary = article_data['article_summary']
            current_article.article_keywords = article_data['article_keywords']
            current_article.article_url = article_data['article_url']

            current_article.save()
        except Exception as e:
            logging.error('Failed for article link-' + str(row['Article_Link']))
            logging.error(e)
            print(e)

    disconnect()


def newyork_data_extraction():
    # All files ending with .xlsx
    files_path = glob.glob(
        "/Users/aryanjadon/Documents/CMPE_255/Backend/data_pipeline/sitemaps/newyork-times-files/*.xlsx")

    for file_name in files_path:
        print(file_name)
        add_records_to_newyork_database(file_name)
        time.sleep(180)


def cnbc_data_extraction():
    # All files ending with .xlsx
    # add file path here - see above function
    files_path = glob.glob("/home/yash/Documents/Fall-2021/abracadata/CMPE_255/Backend/data_pipeline/sitemaps/cnbc-files/*.xlsx")

    for file_name in files_path:
        print(file_name)
        add_records_to_cnbc_database(file_name)
        time.sleep(180)


def latimes_data_extraction():
    # All files ending with .xlsx
    # add file path here - see above function
    files_path = glob.glob("")

    for file_name in files_path:
        print(file_name)
        add_records_to_latimes_database(file_name)
        time.sleep(180)

cnbc_data_extraction()
