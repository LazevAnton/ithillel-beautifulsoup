from pathlib import Path

from service import ScrapeService
import pandas as pd
import app_config


if __name__ == '__main__':
    service = ScrapeService()
    movies = service.get_top_movies()
    tvshow = service.get_top_tvshows()
    df_movies = pd.DataFrame.from_dict(movies)
    df_tvshow = pd.DataFrame.from_dict(tvshow)
    df_tvshow.to_csv(Path(app_config.basedir) / 'top_tvshows.csv')
    # df.to_csv(Path(basedir) / 'top_movies.csv')
