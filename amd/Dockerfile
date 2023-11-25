FROM python:3.8
ADD . /app
COPY . /data
COPY . /src
ADD app.py /app
ADD requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
