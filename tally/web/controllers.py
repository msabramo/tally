from __future__ import absolute_import

from flask import Flask, request, jsonify, render_template

from tally import  counter, record

app = Flask('tally.web')

DEBUG = True

app.config.from_object(__name__)


@app.route("/")
def index():

    all_counters = sorted(list(counter.keys()))
    all_records = sorted(list(record.keys()))

    return render_template("index.html",
        counters=all_counters,
        records=all_records,
    )


@app.route("/api/metric/counter/<slug>", methods=['GET'])
def get_metric_counter(slug):

    c = counter.get(slug)

    d = {
        'name': slug,
        'data': list(c.timestamp_items())
    }

    return jsonify(d)


@app.route("/api/metric/record/<slug>", methods=['GET'])
def get_metric_records(slug):
    pass


@app.context_processor
def inject_debug():
    return dict(debug=DEBUG)
