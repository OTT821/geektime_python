import time
import requests
from bs4 import BeautifulSoup

def main():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    ##这里如果不去定义 header 为字典直接使用是否会报错？
    header['user-agent'] = user_agent
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url, headers=header).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        #all_img_tag
        # all_img_tag = each_movie.find_all('img')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch, headers=header).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')
        # img_tag = all_img_tag[0]

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

# %time main()
start = time.time()
main()
end = time.time()
print('耗时: {:.2f} 秒'.format(end - start))