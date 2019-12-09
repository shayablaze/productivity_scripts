FROM ubuntu as builder
WORKDIR '/app'
RUN apt-get update
RUN apt-get install make
RUN apt-get -y install vim
RUN apt-get -y install gcc
RUN apt-get -y install wget
RUN apt-get -y install curl
RUN apt-get -y install strace
#COPY libhostspriv.so /usr/lib/

COPY . /app/
#COPY Makefile /app/Makefile
RUN chmod 777 /app/do_stuff.sh
#RUN pwd
#RUN ls
RUN /app/do_stuff.sh

#COPY Makefile /app/Makefile
#COPY hosts.c /app/hosts.c
#COPY stam.sh /app/stam.sh
#RUN /app/stam.sh

#COPY do_stuff.sh do_stuff.sh

#COPY /app/libhostspriv.so /usr/lib/
#COPY /app/libhostspriv.so /usr/lib/



FROM ubuntu
WORKDIR '/app'
COPY --from=builder /usr/lib/libhostspriv.so /usr/lib/
RUN apt-get update
RUN apt-get -y install curl
RUN touch aaa
RUN chmod 777 aaa
ARG ROOTLESS_UID=1337
ARG ROOTLESS_GID=0
USER ${ROOTLESS_UID}:${ROOTLESS_GID}
CMD ["/bin/bash"]
