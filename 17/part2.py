"""Day 17: Chronospatial Computer, Part 2

My program's listing is below, along with the actual bitwise operations that
are being performed:

step    prog    operation
 0      bst 4   B = A & 0b111       // Set B to the last 3 bits of A
 2      bxl 2   B = B ^ 0b010       // XOR B with 010
 4      cdv 5   C = A >> B          // Set C to A shifted right by B
 6      bxc 5   B = B ^ C           // XOR B with C
 8      adv 3   A = A >> 3          // Shift A by 3
10      bxl 7   B = B ^ 0b111       // XOR B with 111
12      out 5   out B & 0b111       // Output the last 3 bits of B.
14      jnz 0   goto 0 if A != 0

out: 2, 4, 1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0

A bits:     000 001 010 011 100 101 110 111
B bits:  0. 000 001 010 011 100 101 110 111
         2. 010 011 000 001 110 111 100 101
         4. // C will be 1 for 011, 2 for 010, and 0 in all other cases
         6. 010 011 010 000 110 111 100 101
        10. 101 100 101 111 001 000 011 010
        12. // We now know that the bits in A must be 101.

For each iteration in the loop, we will try all 8 possibilities.
"""

sequence = [0, 3, 5, 5, 7, 1, 3, 0, 5, 4, 5, 7, 2, 1, 4, 2]

A = 0
for n in sequence:
    for bits in range(0, 8):
        A_temp = (A << 3) + bits
        B = A_temp & 7
        B = B ^ 2
        C = A_temp >> B
        B = B ^ C
        B = B ^ 7
        if B & 7 == n:
            A = A_temp
            break

print(A)
