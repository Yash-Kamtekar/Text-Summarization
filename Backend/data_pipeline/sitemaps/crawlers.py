import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


def newyork_times_sitemap():
    newyork_sitemap_url = "https://www.nytimes.com/sitemap/{current_year}/{current_month}/{current_date}/"
    months_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    dates_list = []

    for date in range(1, 32):
        if date < 10:
            dates_list.append("0" + str(date))
        else:
            dates_list.append(str(date))

    for year in ["2020", "2021"]:
        for month in months_list:
            all_article_links = []
            for date in dates_list:
                paper_link = newyork_sitemap_url.format(current_year=year,
                                                        current_month=month,
                                                        current_date=date)
                date_timestamp = year + "-" + month + "-" + date
                try:
                    html_source = urlopen(paper_link)
                    soup = BeautifulSoup(html_source.read(),
                                         'lxml')
                    for ul in soup.find_all('ul', class_='css-cmbicj'):
                        for li in ul.find_all('li'):
                            a_href = li.find('a')
                            all_article_links.append((date_timestamp,
                                                      a_href['href']))
                except Exception as e:
                    print(e)

            file_name = "newyork-times-{year}-{month}.xlsx".format(year=year, month=month)
            newyork_times_articles = pd.DataFrame(all_article_links, columns=['Date', 'Article_Link'])
            newyork_times_articles.to_excel(file_name, index=False)


def yahoo_news_sitemap():
    yahoo_sitemap_url = "http://finance.yahoo.com/sitemap/{current_year}_{current_month}_{current_date}/"
    months_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    dates_list = []

    for date in range(1, 32):
        if date < 10:
            dates_list.append("0" + str(date))
        else:
            dates_list.append(str(date))

    for year in ["2020", "2021"]:
        for month in months_list:
            all_article_links = []
            for date in dates_list:
                paper_link = yahoo_sitemap_url.format(current_year=year,
                                                      current_month=month,
                                                      current_date=date)

                date_timestamp = year + "-" + month + "-" + date
                try:
                    html_source = urlopen(paper_link)
                    soup = BeautifulSoup(html_source.read(),
                                         'lxml')

                    for ul in soup.find_all('ul', class_='Fz(14px) M(0) P(0)'):
                        for li in ul.find_all('li'):
                            a_href = li.find('a')
                            all_article_links.append((date_timestamp,
                                                      a_href['href']))
                except Exception as e:
                    print(e)

            file_name = "yahoo-news-{year}-{month}.xlsx".format(year=year, month=month)
            yahoo_times_articles = pd.DataFrame(all_article_links, columns=['Date', 'Article_Link'])
            yahoo_times_articles.to_excel(file_name, index=False)
            print("File Processed !!")


def la_times_sitemap():
    latimes_sitemap_url = "https://www.latimes.com/sitemap/{current_year}/{current_month}/"
    months_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    for year in ["2020", "2021"]:
        for month in months_list:
            all_article_links = []
            paper_link = latimes_sitemap_url.format(current_year=year,
                                                    current_month=month)
            print(paper_link)
            date_timestamp = year + "-" + month
            try:
                html_source = urlopen(paper_link)
                soup = BeautifulSoup(html_source.read(),
                                     'lxml')

                for ul in soup.find_all('ul', class_='archive-page-menu'):
                    for li in ul.find_all('li'):
                        a_href = li.find('a')
                        all_article_links.append((date_timestamp,
                                                  a_href['href']))
            except Exception as e:
                print(e)

            file_name = "latimes-news-{year}-{month}.xlsx".format(year=year, month=month)
            la_times_articles = pd.DataFrame(all_article_links, columns=['Date', 'Article_Link'])
            la_times_articles.to_excel(file_name, index=False)


def cnbc_sitemap():
    cnbc_sitemap_url = "https://www.cnbc.com/site-map/articles/{current_year}/{current_month}/{current_date}/"
    months_list = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
                   "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
    dates_list = []

    for date in range(1, 32):
        dates_list.append(str(date))

    for year in ["2020", "2021"]:
        for month in months_list:
            all_article_links = []
            for date in dates_list:
                paper_link = cnbc_sitemap_url.format(current_year=year,
                                                     current_month=month,
                                                     current_date=date)

                date_timestamp = year + "-" + months_list[month] + "-" + date
                try:
                    html_source = urlopen(paper_link)
                    soup = BeautifulSoup(html_source, 'html.parser')
                    for div in soup.find_all('div', class_='SiteMapArticleList-articleData'):
                        for li in div.find_all('li'):
                            a_href = li.find('a')
                            all_article_links.append((date_timestamp,
                                                      a_href['href']))
                except Exception as e:
                    print(e)
                file_name = f"cnbc-news-{year}-{months_list[month]}.xlsx"
                cnbc_times_articles = pd.DataFrame(all_article_links, columns=['Date', 'Article_Link'])
                cnbc_times_articles.to_excel(file_name, index=False)
