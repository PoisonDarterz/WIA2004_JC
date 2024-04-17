#include <stdio.h>
#include <stdlib.h>

#define MAX_BLOCKS 50

void allocateFile(int files[], int startBlock, int len) {
    int i;
    for (i = startBlock; i < startBlock + len && i < MAX_BLOCKS; i++) {
        if (files[i] == 0) {
            files[i] = 1; // Allocate block
            printf("Block %d allocated\n", i);
        }
        else {
            printf("Block %d is already allocated\n", i);
        }
    }
    if (i < startBlock + len) {
        printf("Not enough space to allocate the entire file\n");
    }
}

int af() { // change to main if wanna run
    int files[MAX_BLOCKS] = { 0 }; // Initialize all blocks as unallocated

    int startBlock, len, ch;
    do {
        printf("Enter the starting block and the length of the file: ");
        scanf_s("%d %d", &startBlock, &len);

        if (startBlock < 0, startBlock >= MAX_BLOCKS, len <= 0) {
            printf("Invalid input\n");
            continue;
        }

        allocateFile(files, startBlock, len);

        printf("Do you want to enter more files?\n");
        printf("Press 1 for YES, 0 for NO: ");
        scanf_s("%d", &ch);
    } while (ch == 1);

    return 0;
}