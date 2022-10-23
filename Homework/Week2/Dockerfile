FROM python:3.8

Copy . .
WORKDIR /data
# install dependencies
RUN pip install matplotlib
RUN pip install pandas

ADD ../../data/coding-environment-exercise.csv data/coding-environment-excersie.csv
CMD ["python", "./Week2.py"]

#commands to run in the terminal:
# docker build -t yoursuername/plot .
# docker images
# docker run yoursuername/plot
 