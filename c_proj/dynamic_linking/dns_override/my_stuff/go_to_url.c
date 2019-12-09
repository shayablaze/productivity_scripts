// C program to illustrate
// open system call
#include<stdio.h>
#include<fcntl.h>
#include<errno.h>
#include <netdb.h>
extern int errno;
int main()
{
    struct hostent *tmp = 0;
    tmp = gethostbyname("www.google.com");
//    printf("%d", tmp->h_addrtype);
    return 0;
}