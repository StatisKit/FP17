ARG CONDA_VERSION=3
ARG ARCH=64
ARG GIT_TAG=latest
FROM statiskit/linux-${ARCH}:${GIT_TAG}-py${CONDA_VERSION}k

COPY README /home/main/README
COPY .condarc /home/main/.condarc
RUN echo "source activate fp17" >> .bashrc
RUN echo "cat /home/main/README" >> .bashrc

RUN conda create -n fp17 fp17
RUN git clone --recursive https://github.com/StatisKit/FP17
WORKDIR /home/main/FP17/share/jupyter