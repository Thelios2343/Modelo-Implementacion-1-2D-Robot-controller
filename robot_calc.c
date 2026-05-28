#include <string.h>

#define MAX_X  50
#define MIN_X -50
#define MAX_Y  25
#define MIN_Y -25

int calcular_nueva_pos(int x, int y, const char* dir, int pasos,int* nueva_x, int* nueva_y) {
    

    *nueva_x = x;
    *nueva_y = y;

    int candidato;

    if (strcmp(dir, "arriba") == 0) {
        candidato = y + pasos;
        if (candidato > MAX_Y) return 0;
        *nueva_y = candidato;
    } else if (strcmp(dir, "abajo") == 0) {
        candidato = y - pasos;
        if (candidato < MIN_Y) return 0;
        *nueva_y = candidato;
    } else if (strcmp(dir, "derecha") == 0) {
        candidato = x + pasos;
        if (candidato > MAX_X) return 0;
        *nueva_x = candidato;
    } else if (strcmp(dir, "izquierda") == 0) {
        candidato = x - pasos;
        if (candidato < MIN_X) return 0;
        *nueva_x = candidato;
    } else {
        return 0;
    }

    return 1;
}
