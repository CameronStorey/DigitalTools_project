FROM jupyter/base-notebook

COPY . .

# install dependencies
RUN pip install pandas \
	&& pip install numpy \
	&& pip install ipywidgets \
	&& pip install fredapi \
	&& pip install matplotlib \
	&& pip install requests\
	&& pip install datetime\
	&& echo "Installed the packages needed for the Jupyter Notebooks."

#Let's define this parameter to install jupyter lab instead of the default juyter notebook command so we don't have to use it when running the container with the option -e
ENV JUPYTER_ENABLE_LAB=yes


