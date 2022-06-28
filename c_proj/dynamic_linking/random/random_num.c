#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// ran with
// gcc random_num.c -o random_num
//
int main(){
  srand(time(NULL));
  int i = 10;
  while(i--) printf("%d\n",rand()%100);
  return 0;
}