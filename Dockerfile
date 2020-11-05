FROM continuumio/miniconda3:latest

LABEL maintainer="tkolleh <http://kolleh.com>"

COPY ./src /app/src
COPY ./config.ini /app/config.ini
COPY ./environment.yml /tmp/environment.yml

RUN conda env create --file /tmp/environment.yml
# RUN . /opt/conda/etc/profile.d/conda.sh && conda activate

# ENV CONDA_ENVNAME="$(head -1 /tmp/environment.yml | cut -d':' -f2)"

# RUN echo "conda activate $CONDA_ENVNAME" > ~/.bashrc

# ENV PATH /opt/conda/envs/$CONDA_ENVNAME/bin:$PATH

ENV PYTHONPATH "/app:/app/src"

EXPOSE 8181/tcp

WORKDIR /app

ENTRYPOINT ["conda", "run", "-n", "pycrud-person", "python", "src/person_api/run.py"]
# CMD [ "src/person_api/run.py" ]
