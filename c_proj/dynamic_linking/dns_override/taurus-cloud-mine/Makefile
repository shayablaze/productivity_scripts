CFLAGS+=-Wall

all: libhostspriv.so

libhostspriv.so: hosts.c
	$(CC) $(CFLAGS) $(CPPFLAGS) -D_GNU_SOURCE -fPIC -shared hosts.c -o libhostspriv.so -ldl

clean:
	rm -f libhostspriv.so test .hosts
	rm -rf test.dsYM
