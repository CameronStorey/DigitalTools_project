run:
        docker build -t migueldoctor/docker-jupyter-kotlin-notebook .
        docker run --name my-jupyter-kotlin \
        -v /Users/mdoctor/Documents/dockerVolumes/kotlin-jupyter/:/home/jovyan/work \
        -p 8888:8888 \
        migueldoctor/docker-jupyter-kotlin-notebook