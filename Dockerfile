FROM continuumio/anaconda3:latest

LABEL maintainer="tkolleh <http://kolleh.com>"

COPY ./src /app/
COPY ./environment.devenv.yml /tmp/environment.devenv.yml

RUN conda install --yes conda-devenv -c conda-forge
RUN conda devenv --file /tmp/environment.devenv.yml
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate

# Pull the environment name out of the environment.yml
RUN echo "conda activate $(tail -1 /tmp/environment.yml | cut -d'/' -f4)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(tail -1 /tmp/environment.yml | cut -d'/' -f4)/bin:$PATH

EXPOSE 8181/tcp

CMD conda run -n $(tail -1 /tmp/environment.yml | cut -d'/' -f4) gunicorn --bind 0.0.0.0:8181 --timeout 90 --graceful-timeout 90 --keep-alive 4 --workers 2 app.wsgi:patient_flow_service
