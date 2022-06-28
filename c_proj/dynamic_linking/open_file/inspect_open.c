#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
//#include  <netdb.h>
typedef int (*orig_open_f_type)(const char *pathname, int flags);
//struct hostent *gethostbyname(char *name);
int open(const char *pathname, int flags, ...)
{
    /* Some evil injected code goes here. */
    printf("The victim used open(...) to access '%s'!!!\n",pathname);
    orig_open_f_type orig_open;
    orig_open = (orig_open_f_type)dlsym(RTLD_NEXT,"open");
    return orig_open("goo.txt",flags);
}