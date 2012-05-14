from __future__ import absolute_import

from flask import Flask, request, jsonify, render_template

from tally.metric import value_keys, metric_keys, values

app = Flask('tally.web')

DEBUG = True

app.config.from_object(__name__)


@app.route("/")
def index():
    keys = sorted(list(metric_keys()))
    return render_template("index.html", keys=keys)


@app.route("/api/metrics", methods=['GET'])
def list_metrics():
    metrics = [{'name': key} for key in metric_keys()]
    return jsonify(data=metrics)


@app.route("/api/metric/<slug>", methods=['POST'])
def create_metric(slug):
    return "POST"


@app.route("/api/metric/<slug>", methods=['PUT'])
def update_metric(slug):
    return "PUT"


@app.route("/api/metric/<slug>", methods=['DELETE'])
def delete_metric(slug):
    if request.method == 'DELETE':
        return "DELETE"


@app.route("/api/metric/<slug>", methods=['GET'])
def get_metric(slug):

    keys = [k.rsplit(":", 1)[1] for k in value_keys(slug)]
    vals = values(slug)
    data = sorted(list(zip(keys, vals)))

    return jsonify(data=data)


@app.context_processor
def inject_debug():
    return dict(debug=DEBUG)
