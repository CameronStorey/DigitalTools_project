FROM Jupiter/base-notebook

WORKDIR /notebooks

COPY . .

# install dependencies
RUN pip install pandas \
	&& pip install numpy \
	&& pip install ipywidgets \
	&& pip install fredapi \
	&& pip install matplotlib \
	&& pip install requests\
	&& pip install json\
	&& pip install datetime\
	&& pip install os



CMD [ "python", "./your-daemon-or-script.py" ]

#commands to run in the terminal:
# docker build -t yoursuername/plot .
# docker images
# docker run yoursuername/plot
