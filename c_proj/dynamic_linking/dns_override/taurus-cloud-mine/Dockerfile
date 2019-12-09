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
RUN apt-get -y install curl
RUN touch aaa
RUN chmod 777 aaa
COPY dns_override.sh /app/
RUN chmod 777 /app/dns_override.sh
ARG ROOTLESS_UID=1337
ARG ROOTLESS_GID=0
USER ${ROOTLESS_UID}:${ROOTLESS_GID}
CMD ["/bin/bash"]
