from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def status():
    url = request.args.get("url")
    ok = check_status(url)
    status = "deployed" if ok else "failed"
    return app.send_static_file(f"img/heroku-badge-{status}.svg")


def check_status(url: str) -> bool:
    req = requests.get(url)
    return req.ok
