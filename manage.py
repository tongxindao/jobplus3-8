# -*- coding: utf-8 -*-

from simplejob.app import create_app

app = create_app("production")

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=8000, debug=False)
