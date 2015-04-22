#!/usr/bin/env python
import my.settings as settings
import my.logger

log = my.logger.getLogger(__name__, settings.mycomponent['logger'])

def do_things(things):
    log.info("Doing things: %s", things)
