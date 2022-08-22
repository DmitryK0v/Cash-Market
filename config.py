
import logging


DB_NAME = "data/exchange.db"

LOGGER_CONFIG = dict(level=logging.DEBUG,
                     file="data/app.log",
                     formatter=logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s:%(message)s")
                     )