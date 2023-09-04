import logging
import multiprocessing
import sys
from typing import Optional

APP_LOGGER_NAME: str = "ChatApp"
LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_applevel_logger(
    logger_name: str = APP_LOGGER_NAME,
    file_name: Optional[str] = None,
    level: int = logging.DEBUG,
) -> logging.Logger:
    """
    Setup the logger for the application.

    :param logger_name: Name of the logger.
    :param file_name: Name of the log file.
    :param level: Logging level.
    :return: Configured logger.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    formatter = logging.Formatter(LOG_FORMAT)

    # Check if a StreamHandler exists
    if not any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers
    ):
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    if file_name:
        try:
            fh = logging.FileHandler(file_name)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        except Exception as e:
            logger.warning(f"Could not add file handler: {e}")

    return logger


def get_multiprocessing_logger(
    file_name: Optional[str] = None, level: int = logging.DEBUG
) -> logging.Logger:
    """
    Setup the logger for the application for multiprocessing.

    :param file_name: Name of the log file.
    :param level: Logging level.
    :return: Configured logger.
    """
    logger = multiprocessing.get_logger()
    logger.setLevel(level)
    formatter = logging.Formatter(LOG_FORMAT)

    # Check if a StreamHandler exists
    if not any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers
    ):
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    if file_name:
        try:
            fh = logging.FileHandler(file_name)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        except Exception as e:
            logger.warning(f"Could not add file handler: {e}")

    return logger


def get_logger(
    module_name: str, logger_name: Optional[str] = None, level: int = logging.DEBUG
) -> logging.Logger:
    """
    Get the logger for the module.

    :param module_name: Name of the module.
    :param logger_name: Name of the logger.
    :param level: Logging level.
    :return: Configured logger.
    """
    logger = logging.getLogger(logger_name or APP_LOGGER_NAME).getChild(module_name)
    logger.setLevel(level)
    return logger
