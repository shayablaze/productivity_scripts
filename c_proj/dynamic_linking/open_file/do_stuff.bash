rm foo.txt
rm read_something
rm -rf *.o
gcc read_something.c -o read_something
gcc -shared -fPIC  inspect_open.c -o inspect_open.so -ldl
echo "now regular"
./read_something
rm foo.txt
echo "now with preload"
LD_PRELOAD=$PWD/inspect_open.so ./read_something