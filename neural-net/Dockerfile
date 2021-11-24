FROM arm64v8/python:3.8-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF.8

# Install base utilities
RUN apt-get update && \
    apt-get install -y build-essential  && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install streamlit
RUN pip3 install torch