Contrived example usage of python logger
========================================

Demonstration purposes only. This is perhaps a little unwieldly for most/some
purposes. It demonstrates a settings.py to configure loggers; then using a
custom logger which prefixes all log messages with a timestamp, log level, and
the calling module/function name. This can be useful in verbose debug output,
it's worth configuring a more concise output format for production use
especially when the user's rsyslog daemon will already prefix log lines with a
timestamp anyway...

Example invocations
-------------------

Show output from both configured stderr/stdout loggers configured in my.settings:

    $ ./mycomponent.py 
    2015-04-22 17:14:27,034 DEBUG   __main__.<module>()     blah blah from __main__, calling do_stuff("things")
    2015-04-22 17:14:27,034 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
    2015-04-22 17:14:27,034 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
    2015-04-22 17:14:27,035 INFO    my.foo.do_things()      Doing things: things

or redirect STDOUT so we're left with just STDERR logger:

    $ ./mycomponent.py >/dev/null
    2015-04-22 17:15:27,643 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")

or redirect STDERR so we're left with just STDOUT logger:

    $ ./mycomponent.py 2>/dev/null
    2015-04-22 17:16:30,259 DEBUG   __main__.<module>()     blah blah from __main__, calling do_stuff("things")
    2015-04-22 17:16:30,259 ERROR   __main__.do_stuff()     blah from do_stuff(), calling my.foo.do_things("things")
    2015-04-22 17:16:30,259 INFO    my.foo.do_things()      Doing things: things
