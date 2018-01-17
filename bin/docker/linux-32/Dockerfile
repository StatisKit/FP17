ARG CONDA_VERSION=2
ARG GIT_TAG=latest
FROM statiskit/linux-32:${GIT_TAG}-py${CONDA_VERSION}k

COPY README /home/main/README
RUN rm /home/main/.condarc
COPY .condarc /home/main/.condarc
RUN conda install -n $CONDA_DEFAULT_ENV fp17
UN echo "source activate fp17" >> .bashrc
RUN echo "cat /home/main/README" >> .bashrc

RUN conda create -n fp17 fp17
RUN git clone --recursive https://github.com/StatisKit/FP17
WORKDIR /home/main/FP17/share/jupyter