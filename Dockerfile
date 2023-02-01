FROM python:3.10

EXPOSE 8000

WORKDIR /TimezoneDB

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

