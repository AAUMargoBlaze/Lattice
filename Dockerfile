FROM python:3.9

RUN pip install graphviz
RUN pip install lattice-graph-manipulation
RUN apt update
RUN apt install -y graphviz
RUN apt install -y xdg-utils
RUN apt install -y libgraph-easy-perl

ENTRYPOINT ["python"]