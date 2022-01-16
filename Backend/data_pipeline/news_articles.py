import json
import requests
import logging
# third party imports
from newspaper import Article
import xmltodict


# function to parse web articles
def parse_article(article_url):
    """
    Author - Aryan Jadon
    function which extracts information given a web url

    :param article_url: article url
    :return: json record
    """

    # passing the article url
    article = Article(article_url)

    # downloading the data
    article.download()

    # parsing the article
    article.parse()

    # processing natural language processing on article
    article.nlp()

    # creating a json record
    article_record = {
        "article_title": article.title,  # article title
        "article_authors": article.authors,  # article authors
        "article_published_date": str(article.publish_date),  # article published data
        "article_text": article.text,  # article web text
        "images_link": article.top_image,  # article image link
        "video_link": article.movies,  # article video link
        "article_summary": article.summary,  # article summary
        "article_keywords": article.keywords,  # keywords associated with articles
        "article_url": article_url  # article url
    }

    # return json record
    return article_record


# function to extract all article web links
def extract_rss_feeds(xml_url, *header_value):
    """
    Author - Aryan and Swathi
    function to extract all article web links from an xml file

    :param xml_url: xml link
    """
    if len(header_value):
        for value in header_value:
            response = requests.get(xml_url, headers=value)
    else:
        response = requests.get(xml_url)
        
    # getting the web page data

    # parsing and storing the data in to a dictionary
    dict_data = xmltodict.parse(response.content)

    # getting all the items from rss
    all_parsed_items = dict_data['rss']['channel']['item']

    # list to store all href
    all_href_links = []

    # iterating through all the parsed items
    for index, values in enumerate(all_parsed_items):
        # getting and storing
        link_href = all_parsed_items[index]['link']
        all_href_links.append(link_href)

    all_articles_records = {}

    # iterating all the links
    for href_link in all_href_links:
        try:
            # passing the article link to parsing function
            article_data = parse_article(href_link)

            # storing the results from functions from dictionary
            all_articles_records[href_link] = article_data
        except Exception as e:
            # logging the error
            logging.error('This is an error message')

    return all_articles_records


if __name__ == '__main__':
    '''
    # initializing the logger
    logging.basicConfig(filename='Logs/news_articles.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')

    # new york times rss feed links
    with open('rss_sources/newyork_times.json') as f:
        new_york_times_rss = json.load(f)

    # CNBC rss feed links
    with open('rss_sources/CNBC.json') as f:
        cnbc_rss_feeds = json.load(f)

    # la times rss feed links
    with open('rss_sources/la_times.json') as f:
        la_times_feeds = json.load(f)

    # iterating through all rss links
    for key, value in new_york_times_rss.items():
        print(key)
        # extracting news
        fetched_new_york_records = extract_rss_feeds(value)

    for key, value in cnbc_rss_feeds.items():
        print(key)
        # extracting news
        fetched_cnbc_records = extract_rss_feeds(value)

    for key, value in la_times_feeds.items():
        print(key)
        header_def = {
            "user-agent": "Mozilla/5.0",
        }
        fetched_la_records = extract_rss_feeds(value, header_def)

    print(fetched_cnbc_records)
    print(fetched_new_york_records)
    print(fetched_la_records)
    '''
