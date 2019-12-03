all: main.o function.o
	 gcc -o Binary main.o function.o
main.o: main.c
	gcc -c main.c -I ./
function.o: function.c
	gcc -c function.c -I ./
clean:
	rm -rf *.o
	rm -rf Binary
