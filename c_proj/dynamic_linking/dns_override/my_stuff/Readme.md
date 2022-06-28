rm foo.txt
gcc read_something.c -o read_something
// run random_num

gcc -shared -fPIC  inspect_open.c -o inspect_open.so -ldl

// run 
// LD_PRELOAD=$PWD/inspect_open.so ./read_something
// or
// export LD_PRELOAD=$PWD/inspect_open.so
// read_something