
FROM python:3.9.18-slim

WORKDIR /api

COPY . /api

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
