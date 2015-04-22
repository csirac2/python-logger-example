#!/usr/bin/env python
import logging

mycomponent = {
    'logger' : {
        'stdout' : {
            'format' : "%(asctime)s %(levelname)s\t%(name)s.%(funcName)s()\t%(message)s",
        },
        'stderr' : {
            'level' : logging.ERROR,
            'format' : "%(asctime)s %(levelname)s\t%(name)s.%(funcName)s()\t%(message)s",
        },

        # Default level of the various loggers if they're not specified
        'level' : logging.DEBUG,
    },
}
