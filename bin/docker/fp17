ARG CONDA_VERSION=2
ARG GITHUB_USER=statiskit
ARG GITHUB_REPO=fp17
FROM "statiskit/ubuntu:latest-py"$CONDA_VERSION"k"
ARG CONDA_VERSION
ARG GITHUB_USER
ARG GITHUB_REPO

RUN git clone --recursive https://github.com/$GITHUB_USER/$GITHUB_REPO.git repository
RUN conda env update -n root -f repository/environment.yml
RUN conda download repository -c statiskit
RUN mkdir $HOME/channel
RUN cp -rf $HOME/miniconda/pkgs $HOME/channel/linux-64
RUN cd $HOME/channel/linux-64 && conda index
RUN echo "channels:" >> $HOME/.condarc
RUN echo "  - file:///"$HOME"/channel"
RUN echo "allow_other_channels: False" >> $HOME/.condarc
RUN echo "auto_update_conda: False" >> $HOME/.condarc

RUN echo "echo \"##############################################################################\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"# Welcome to the Docker container that enables you to run examples presented #\"" >> $HOME/.bashrc
RUN echo "echo \"# in the AutoWIG paper. After launching this container using the following   #\"" >> $HOME/.bashrc
RUN echo "echo \"# commmand line,                                                             #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"#    docker run -i -t -p 8888:8888 "$GITHUB_USER"/"$GITHUB_REPO":latest-py"$CONDA_VERSION"k                #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"# you can run examples as follows,                                           #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"# 1. Launch the Jupyter notebook with the following command                  #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"#        jupyter notebook --ip='*' --port=8888 --no-browser                  #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"# 2. Copy the URL given in the terminal and paste it in your browser.        #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"# 3. Click on the notebooks you want to run (denoted by *.ipynb) and then    #\"" >> $HOME/.bashrc
RUN echo "echo \"#    click on Run All item of the Cell top menu bar.                         #\"" >> $HOME/.bashrc
RUN echo "echo \"#                                                                            #\"" >> $HOME/.bashrc
RUN echo "echo \"##############################################################################\"" >> $HOME/.bashrc

RUN echo "source activate root" >> $HOME/.bashrc
RUN echo "export CPU_COUNT=1" >> $HOME/.bashrc

WORKDIR /home/main/repository/share/jupyter
