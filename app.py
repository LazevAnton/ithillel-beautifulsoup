from service import ScrapeService
import pandas as pd


if __name__ == '__main__':
    service = ScrapeService()
    movies = service.get_top_movies()
    df = pd.DataFrame.from_dict(movies)
    # df.to_csv(Path(basedir) / 'top_movies.csv')
