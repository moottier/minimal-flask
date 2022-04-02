import logging, sys

def create_logger() -> logging.Logger:
    """Create a logger that outputs all log levels to stdout

    Outputs with format: {{TIME}} - {{MODULE_SRC}} - {{LINE_NO}} - {{LEVEL}} - {{MSG}}
        {{TIME}}       time the message sent
        {{MODULE_SRC}} name of the module sending the message
        {{LINE_NO}}    line number in the module that sent the message
        {{LEVEL}}      log-level (DEBUG/INFO/WARNING/ERROR/CRITICAL)
        {{MSG}}        the message
    """
    log_level = logging.DEBUG

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)

    format = '%(asctime)s - %(module)s : %(lineno)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format, style='%')
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
