FROM python:3.8.5
WORKDIR /opt/app
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]