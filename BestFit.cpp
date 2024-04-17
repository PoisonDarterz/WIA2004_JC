#include <iostream>
#include <vector>


struct Block {
    int size;  // Size of the memory block
    Block* next;  // Pointer to the next block in the linked list
};

/**
 * bestFit function takes a pointer to the head of the block linked list
 * and a vector of process sizes. It iterates through each process size and
 * tries to find the best-fitting block (smallest block that can hold the process)
 * from the linked list.
 *
 * @param head - pointer to the head of the block linked list
 * @param processSize - vector containing sizes of processes to be allocated
 */
void bestFit(Block* head, std::vector<int> processSize) {
    // Traverse the process list (loop through each process size)
    for (int process : processSize) {
        Block* bestBlock = nullptr;  // Pointer to the best-fitting block (initially null)
        Block* current = head;         // Pointer to traverse the block linked list

        // Find the best-fitting block for the current process
        while (current != nullptr) {
            // Chec k if current block can hold the process and Check for best fit
            if (current->size >= process && (bestBlock == nullptr || current->size < bestBlock->size)) {
                bestBlock = current;
            }
            current = current->next;  // Move current pointer to the next block in the list
        }

        // Allocate process if a fitting block is found
        if (bestBlock) {
            std::cout << "Process " << process << " allocated to block " << bestBlock->size << std::endl;
            bestBlock->size -= process;  // Update the size of the block after allocation
        }
        else {
            std::cout << "Process " << process << " not allocated - Insufficient memory" << std::endl;
        }
    }
}

int main() { // change to main if wanna run
    // Create linked list of blocks (modify as needed for your block sizes)
    Block* head = new Block{ 100, nullptr };
    head->next = new Block{ 50, nullptr };
    head->next->next = new Block{ 200, nullptr };
    head->next->next->next = new Block{ 300, nullptr };

    std::vector<int> processSize = { 212, 417, 112, 49 };
    bestFit(head, processSize);

    // Deallocate memory
    Block* current = head;
    while (current != nullptr) {
        Block* temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}
