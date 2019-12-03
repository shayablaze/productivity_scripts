rm random_num
rm -rf *.o
gcc random_num.c -o random_num
gcc -shared -fPIC unrandom.c -o unrandom.so
echo "now regular"
./random_num
echo "now with preload"
LD_PRELOAD=$PWD/unrandom.so ./random_num