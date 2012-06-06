from __future__ import absolute_import

from sys import path

from flask import Flask
from unipath import FSPath as Path

TALLY_DIR = Path(__file__).absolute().ancestor(2)
path.append(TALLY_DIR)

from tally import counter, record

app = Flask(__name__)
DEBUG = True
app.config.from_object(__name__)


@app.route("/")
@record("index render")
def index():

    count = len(counter.get("index view"))
    render_metric = record.get("index render")
    minimum_val = render_metric.min()
    maximum_val = render_metric.max()

    counter.incr("index view")

    return """
    %s<br/>
    <br/>
    %s - min<br/>
    %s - max
    """ % (count, minimum_val, maximum_val)


def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()
