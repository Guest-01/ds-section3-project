FROM python:3.8

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt && python -c "from three_line import db, create_app;db.create_all(app=create_app())"

EXPOSE 8000

CMD [ "gunicorn" ]