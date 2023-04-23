from service import ScrapeService
from pathlib import Path
import pandas as pd
from app_config import basedir


if __name__ == '__main__':
    service = ScrapeService()
    movies = service.get_top_movies()
    df = pd.DataFrame.from_dict(movies)
    df.to_csv(Path(basedir) / 'top_movies.csv')
