FROM python:3.10.2-slim

# Set the working directory to your application directory
WORKDIR /home/python/app

# Python
COPY . /home/python/app

RUN pip install -r requirements.txt

CMD ["/home/python/app/app.py"]
ENTRYPOINT [ "python" ]