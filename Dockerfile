FROM python:3

COPY . .

RUN pip install Flask

CMD ["python", "main.py"]