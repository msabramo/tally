from __future__ import absolute_import

from tally.web.controllers import app


def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()
