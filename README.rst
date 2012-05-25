Tally
========================================

Tally is an analytics tool for Python. At the moment it is Redis powered but
written in a way to allowcustom backends and may support more in future.

Tally comes with tools to store metrics and a flask and D3 powered UI to view
them.


Installation
========================================


    pip install tally


Recording Stats
========================================

The simplest usage of tally is the following.

    from tally import metric
    metric.incr("my stat name")

This will will simple record a increment on the counter each time its called.

You can also do this with a decorator. In the following example each time the
home method is called, the counter will be incremented.

    from tally import metric

    @metric.counter("my stat name")
    def home():
        pass

Tally also supports storing integer numbers. This can be done in two ways, by
directly calling the function

    from tally import metric
    metric.record("processing time", 16)

You can also use a decorator, in a similar way to the countr.

    from tally import metric

    @metric.timer("processing time")
    def calculate_pi():
        pass


Showing Reports
========================================

Tally also comes with a simple Flask app for viewing stats and a number of
helpers so you can integrate them easily into your own applications.

