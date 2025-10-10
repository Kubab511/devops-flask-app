#ifndef FUNCTIONS_H
#define FUNCTIONS_H

// Macros for accessing and modifying the grid
#define CELL(I,J) (field[size*(I)+(J)])
#define ALIVE(I,J) t[size*(I)+(J)] = 1
#define DEAD(I,J)  t[size*(I)+(J)] = 0

// Function declarations (prototypes)
int count_alive(const char *field, int i, int j, int size);
void evolve(const char *field, char *t, int size);

#endif