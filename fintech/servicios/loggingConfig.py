import logging



logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(asctime)s | %(message)s"
)


def log(tipo, msj):
    logger_method = getattr(logging, tipo.lower())
    logger_method(msj)


