gcc random_num.c -o random_num
// run random_num

gcc -shared -fPIC unrandom.c -o unrandom.so
// run 
// LD_PRELOAD=$PWD/unrandom.so ./random_num
// or
// export LD_PRELOAD=$PWD/unrandom.so
// random_num