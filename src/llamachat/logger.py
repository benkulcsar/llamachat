import logging


def get_logger() -> logging.Logger:
    """
    Configures logging and returns a named logger for llamachat.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger("llamachat")
