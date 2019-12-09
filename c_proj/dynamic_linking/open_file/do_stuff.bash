#rm foo.txt
rm read_something
rm -rf *.o
gcc go_to_url.c -o read_something
gcc -shared -fPIC  dns_override.c -o inspect_open.so -ldl
echo "now regular"
./read_something
#rm foo.txt
echo "now with preload"
#LD_PRELOAD=$PWD/inspect_open.so ./read_something
export LD_PRELOAD=$PWD/inspect_open.so
./read_something
#curl -L http://www.google.com