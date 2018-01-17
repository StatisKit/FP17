ARG CONDA_VERSION=2
ARG GIT_TAG=latest
FROM statiskit/linux-32:${GIT_TAG}-py${CONDA_VERSION}k

COPY README /home/main/README
RUN rm /home/main/.condarc
COPY .condarc /home/main/.condarc
RUN conda install -n $CONDA_DEFAULT_ENV fp17
RUN echo "cat /home/main/README" >> .bashrc

COPY release.sh /home/main/release.sh
COPY deploy.sh /home/main/deploy.sh

WORKDIR /home/main/FP17/share/jupyter