FROM python:3
LABEL maintainer="Umang Shrestha <umangshrestha09@gmail.com>"
WORKDIR /WORK_REPO
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]


