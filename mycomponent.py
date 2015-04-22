#!/usr/bin/env python
import my.foo
import my.settings as settings
import my.logger

log = my.logger.getLogger(__name__, settings.mycomponent['logger'])

def do_stuff(things):
    log.error('blah from do_stuff(), calling my.foo.do_things("%s")', things)
    my.foo.do_things(things)

if __name__ == '__main__':
    log.debug('blah blah from __main__, calling do_stuff("things")')
    do_stuff('things')

# Example invocations
#
# Both of the configured stderr/stdout loggers configured in my.settings:
#
# $ ./mycomponent.py 
# 2015-04-22 17:14:27,034 DEBUG   __main__.<module>()     blah blah from __main__, calling do_stuff("things")
# 2015-04-22 17:14:27,034 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
# 2015-04-22 17:14:27,034 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
# 2015-04-22 17:14:27,035 INFO    my.foo.do_things()      Doing things: things
#
# or redirect STDOUT so we're left with just STDERR logger:
#
# $ ./mycomponent.py >/dev/null
# 2015-04-22 17:15:27,643 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
#
# or redirect STDERR so we're left with just STDOUT logger:
#
# $ ./mycomponent.py 2>/dev/null
# 2015-04-22 17:16:30,259 DEBUG   __main__.<module>()     blah blah from __main__, calling do_stuff("things")
# 2015-04-22 17:16:30,259 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
# 2015-04-22 17:16:30,259 INFO    my.foo.do_things()      Doing things: things
