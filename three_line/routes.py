from flask import Blueprint, flash, redirect, render_template, request, url_for

from three_line import db
from three_line.models import Summary
from three_line.utils import api_call
from pickle import dumps, loads

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("home.html")


@bp.route("/summarize", methods=["POST"])
def summarize():
    title = request.form.get("title")
    content = request.form.get("content")

    if title:
        result = api_call(content, title=title)
    else:
        result = api_call(content)

    if "summary" in result.keys():  # means success
        sentences = result["summary"].split("\n")
        summary = Summary(
            title=title,
            content=content,
            result_1=sentences[0],
            result_2=sentences[1],
            result_3=sentences[2],
        )
        db.session.add(summary)
        db.session.commit()
        for sentence in sentences:
            flash(sentence)
    else:  # means error
        flash(result)

    return redirect(url_for("main.home"))


@bp.route("/history")
def history():
    summaries = Summary.query.all()

    return render_template("history.html", data=summaries)


@bp.route("/update")
def update():
    pass
