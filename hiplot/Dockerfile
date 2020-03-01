FROM jupyter/datascience-notebook

WORKDIR /app

COPY fetchers.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["bash", "-c",  "hiplot fetchers.fetch_local_csv_experiment --host 0.0.0.0 --port 5005"]