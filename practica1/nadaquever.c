#include <stdio.h>

int main() {
    int a = 3;
    int b = 3;
    int d = 3;
    int c = a^b;
    printf("%d\n", c);
    char ch;
    while ( ( ch=getchar() ) != EOF ) {
      printf("%c\n", ch);
    }
    return 0;
}