#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <netdb.h>
//#include  <netdb.h>
//typedef int (*orig_open_f_type)(const char *pathname, int flags);

//struct hostent *gethostbyname(char *name);
//int open(const char *pathname, int flags, ...)
//{
//    /* Some evil injected code goes here. */
//    printf("The victim used open(...) to access '%s'!!!\n",pathname);
//    orig_open_f_type orig_open;
//    orig_open = (orig_open_f_type)dlsym(RTLD_NEXT,"open");
//    return orig_open("goo.txt",flags);
//}

typedef struct hostent *(*orig_gethostbyname_f_type)(const char *name);
struct hostent *gethostbyname(const char *name)
{
    printf ("in get host by name override EVIL!!!!!\n");
    orig_gethostbyname_f_type orig_gethostbyname;
    orig_gethostbyname = (orig_gethostbyname_f_type)dlsym(RTLD_NEXT,"gethostbyname");
    return  orig_gethostbyname(name);
}
