#include<stdio.h>
#include<string.h>

int main() {
  char p[100],q[100];
  int i,j,n,s=0;
  scanf("%s\t%s",p,q);
  n=strlen(q);
  for(i=0;i<n;i++)
  {
    for(j=0;j<i;j++);
    {
      if(p[i]!=q[j])
      {
        s++;
      }
    }
  }
    printf("%d",s);
     return 0;
}
