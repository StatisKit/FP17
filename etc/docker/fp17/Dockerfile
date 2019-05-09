ARG CONDA_VERSION=3
ARG ARCH=64
ARG GIT_TAG=latest
FROM statiskit/linux-${ARCH}:${GIT_TAG}-py${CONDA_VERSION}k

RUN echo ${HOME}
RUN ls ${HOME}

COPY README ${HOME}/README
COPY .condarc ${HOME}/.condarc
RUN more ${HOME}/.condarc
RUN echo "source activate fp17" >> .bashrc
RUN echo "cat ${HOME}/README" >> .bashrc

RUN conda create -n fp17 fp17
RUN git clone --recursive https://github.com/StatisKit/FP17
WORKDIR ${HOME}/FP17/share/jupyter