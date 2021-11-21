FROM arm64v8/python:3.8-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF.8

ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="true"

# ERROR:  wget: not found
# TODO fix this error
RUN cd && wget -O Miniforge3.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh && \
    bash Miniforge3.sh -b && \
    rm Miniforge3.sh

ENV PATH /home/vscode/miniforge3/bin:$PATH

RUN conda install streamlit