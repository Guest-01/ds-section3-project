from flask import Blueprint, flash, redirect, render_template, request, url_for

from three_line import db
from three_line.models import Summary
from three_line.utils import api_call
from pickle import dumps, loads

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("home.html")


@bp.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
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
            # TODO: 에러메시지 한글화
            flash(result)

        return redirect(url_for("main.summarize"))
    return render_template("summarize.html")


@bp.route("/history")
def history():
    summaries = Summary.query.order_by(Summary.create_date.desc())

    return render_template("history.html", data=summaries)


@bp.route("/update/<int:summary_id>", methods=['GET', 'POST'])
def update(summary_id):
    summary = Summary.query.get(summary_id)
    if request.method == 'POST':
        summary.title = request.form.get("title")
        summary.result_1 = request.form.get("result_1")
        summary.result_2 = request.form.get("result_2")
        summary.result_3 = request.form.get("result_3")
        summary.modified = "수정됨"
        db.session.commit()
        flash(f"{summary_id}번 요약본을 수정하였습니다")
        return redirect(url_for('main.history'))
    return render_template('update.html', data=summary)


@bp.route("/delete/<int:summary_id>")
def delete(summary_id):
    s = Summary.query.get(summary_id)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for("main.history"))
