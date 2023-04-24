import requests
from bs4 import BeautifulSoup


class ScrapeService:
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34"
                      " (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"

    }
    FILMS_URL = "https://www.imdb.com/chart/top"
    TVSHOWS_URL = "https://www.imdb.com/chart/tvmeter"

    def get_top_movies(self):
        req = requests.get(self.FILMS_URL, self.headers)
        soup = BeautifulSoup(req.content, 'lxml')
        poster_tag = soup.find_all('td', class_='posterColumn')
        title_tag = soup.find_all('td', class_='titleColumn')
        rating_tag = soup.find_all('td', class_='ratingColumn imdbRating')

        assert len(poster_tag) == len(title_tag) == len(rating_tag) == 250, 'Something went wrong'

        movies_result = []
        for data in range(len(poster_tag)):
            posters = self.get_poster(tag=poster_tag[data])
            title = self.get_title(tag=title_tag[data])
            year = self.get_year(tag=title_tag[data])
            rating = self.get_rating(tag=rating_tag[data])

            movies_result.append(
                {
                    'Poster': posters,
                    'Title': title,
                    'Year': year,
                    'Rating': rating
                }
            )
        return movies_result

    def get_poster(self, tag):
        return tag.find('img')['src']

    def get_title(self, tag):
        return tag.find('a').text.strip()

    def get_year(self, tag):
        return int(tag.find('span').text.lstrip('(').rstrip(')').strip())

    def get_rating(self, tag):
        if tag.find('strong') is None:
            return 0
        return float(tag.find('strong').text.strip())

    def get_top_tvshows(self):
        req = requests.get(self.TVSHOWS_URL, self.headers)
        soup = BeautifulSoup(req.content, 'lxml')
        tvshows_poster_tag = soup.find_all('td', class_='posterColumn')
        tvshows_title_tag = soup.find_all('td', class_='titleColumn')
        tvshows_rating_tag = soup.find_all('td', class_='ratingColumn imdbRating')

        tvshows_result = []
        for tvshow in range(len(tvshows_poster_tag)):
            tv_posters = self.get_poster(tag=tvshows_poster_tag[tvshow])
            tv_title = self.get_title(tag=tvshows_title_tag[tvshow])
            tv_year = self.get_year(tag=tvshows_title_tag[tvshow])
            tv_rating = self.get_rating(tag=tvshows_rating_tag[tvshow])
            tvshows_result.append(
                {
                    'Posters': tv_posters,
                    'Title': tv_title,
                    'Year': tv_year,
                    'Rating': tv_rating
                }
            )
        return tvshows_result
