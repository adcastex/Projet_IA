FROM python:3.11-slim

RUN mkdir /App
COPY App /App
COPY requirements.txt /App/requirements.txt

WORKDIR /App 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --verbose
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

CMD ["streamlit","run", "accueil.py"]
