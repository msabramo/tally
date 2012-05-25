Tally
========================================

Tally is an analytics package for Python. It's powered by Redis but with plan
to support other backends in the future. Tally comes with tools to store
metrics and a flask and D3 powered UI to view them.

Tally currently supports two different metric forms, counters and records.
Counters simply store a number against a key that is incremented and timers
store a set of numbers against a key. Both are stored with the time of the
event to how data as a time series.

As an example use case, counters could be used to record how often a specific
API call is made or how often users are registering. Records could be used to
record the processing time of a request or the number of items being added to
a users shopping basket.


Installation
========================================

Use pip::

    pip install tally


Recording Stats
========================================

The simplest usage of tally is the following::

    from tally import counter
    counter.incr("my stat name")

This will will simple record a increment on the counter each time its called.

You can also do this with a decorator. In the following example each time the
home method is called, the counter will be incremented::

    from tally import counter

    @counter("my stat name")
    def home():
        pass

Tally also supports storing integer numbers. This can be done in two ways, by
directly calling the function::

    from tally import record
    record.add("processing time", 16)

You can also use a decorator, in a similar way to the countr::

    from tally import record

    @record("processing time")
    def calculate_pi():
        pass


Showing Reports
========================================

Tally also comes with a simple Flask app for viewing stats and a number of
helpers so you can integrate them easily into your own applications.

