rm -rf *.so
gcc -shared -fPIC  dns_override.c -o dns_override.so -ldl
#echo "now with preload"
#strace ls &> a.txt
export LD_PRELOAD=$PWD/dns_override.so
gcc go_to_url.c -o go_to_url
./go_to_url
curl -L http://www.google.com