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


@app.route("/metrics", methods=['GET'])
def list_metrics():
    return jsonify(data=list(metric_keys()))


@app.route("/metric/<slug>", methods=['POST'])
def create_metric(slug):
    return "POST"


@app.route("/metric/<slug>", methods=['PUT'])
def update_metric(slug):
    return "PUT"


@app.route("/metric/<slug>", methods=['DELETE'])
def delete_metric(slug):
    if request.method == 'DELETE':
        return "DELETE"


@app.route("/metric/<slug>", methods=['GET'])
def get_metric(slug):
    return jsonify(keys=value_keys(slug), values=values(slug))
