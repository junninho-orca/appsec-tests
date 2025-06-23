#include <stdio.h>

void vulnerable_function() {
    char buffer[50];
    printf("Enter your name: ");
    // Vulnerable to buffer overflow
    gets(buffer);
    printf("Hello, %s\n", buffer);
}

int main() {
    vulnerable_function();
    return 0;
} 