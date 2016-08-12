import logging
import sys

try:
    from ipcalcng.version import version
    IPCALCNG_VERSION = version.ipcalcng_version
except ImportError:
    IPCALCNG_VERSION = "0.0.unknown.0"


def setup_logger():
    """
    Setup the logging classes for normal operation. Opens a syslog logger, and a standard output/error channel
    logger. This function must be called once and the global log handle should point to it's return value.
    :return: log handle
    """
    log = logging.getLogger()
    stdout_logger = logging.StreamHandler(sys.stdout)

    log.setLevel(logging.WARNING)

    stdout_formatter = logging.Formatter('%(levelname)s %(funcName)-20s: %(message)s',
                                        datefmt="%H:%M:%S")

    stdout_logger.setFormatter(stdout_formatter)

    log.addHandler(stdout_logger)
    return log


def set_log_debug():
    log.setLevel(logging.DEBUG)


def set_log_info():
    log.setLevel(logging.INFO)

log = setup_logger()
