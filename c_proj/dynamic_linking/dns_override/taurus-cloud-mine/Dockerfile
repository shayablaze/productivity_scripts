FROM ubuntu as builder
WORKDIR '/app'
RUN apt-get update
RUN apt-get install make
RUN apt-get -y install gcc
COPY . /app/
RUN chmod 777 /app/configure_shared_object.sh
RUN /app/configure_shared_object.sh


FROM ubuntu
WORKDIR '/app'
COPY --from=builder /usr/lib/libhostspriv.so /usr/lib/
RUN apt-get update
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get -y install curl
RUN touch '/app/aaa'
RUN chmod 777 '/app/aaa'
COPY dns_override.sh /app/
COPY python_proj /app/python_proj
RUN chmod 777 /app/dns_override.sh
ARG ROOTLESS_UID=1337
ARG ROOTLESS_GID=0
USER ${ROOTLESS_UID}:${ROOTLESS_GID}
CMD ["/bin/bash"]
