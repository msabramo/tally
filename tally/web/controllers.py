from __future__ import absolute_import

from datetime import datetime
from time import mktime

from flask import Flask, request, jsonify, render_template

from tally.metric import  counters, records, values, keyring

app = Flask('tally.web')

DEBUG = True

app.config.from_object(__name__)


@app.route("/")
def index():
    all_counters = sorted(list(counters()))
    all_records = sorted(list(records()))
    return render_template("index.html", counters=all_counters, records=all_records)


@app.route("/api/metric/<slug>", methods=['GET'])
def get_metric(slug):

    keys = [k.rsplit(":", 1)[1] for k in keyring(slug)]
    vals = values(slug)

    if 'daily' in request.args:
        keys = [mktime(datetime.fromtimestamp(float(str(key))).date().timetuple()) for key in keys]
        data = {}
        for i, key in enumerate(keys):
            data[key] = data.get(key, 0) + int(vals[i])
        data = sorted(list(data.items()))
    else:
        data = sorted(list(zip(keys, vals)))

    return jsonify(data=data)


@app.context_processor
def inject_debug():
    return dict(debug=DEBUG)
