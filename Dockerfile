FROM python:3.9.9
RUN pip install Flask
ADD TPCloudAnimals /
VOLUME /var/lib/TPCloudAnimals
CMD python frontend/app.py
