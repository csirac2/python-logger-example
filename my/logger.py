import logging
import sys

def getStreamHandler(logger, name, config, stream):
    handler = logging.StreamHandler(stream=stream)
    if 'format' in config:
        handler.setFormatter(logging.Formatter(config['format']))
    if 'level' in config:
        handler.setLevel(config['level'])

    return handler

def getLogger(name, config):
    logger = logging.getLogger(name)
    
    logger.addHandler(
            getStreamHandler(logger, name, config['stdout'], sys.stdout))
    logger.addHandler(
            getStreamHandler(logger, name, config['stderr'], sys.stderr))
    logger.setLevel(config['level'])

    return logger
