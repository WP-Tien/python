"""
permute: Hoán vị
pocket: Túi
"""

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(permute("ABC", ""))

# CBA
# BCA
# CAB
# ACB
# BAC
# ABC
# None

""" 
    => ABC, "" length = 3
        i = 0; letter = A; front = ''; back = BC; together = BC
            => BC, "A" length = 2
                i = 0; letter = B; front = ''; back = C; together = C
                    => C, "BA" length = 1
                        i = 0; letter = C; front = ''; back = ''; together = ''
                            => '', "CBA"
                                => CBA
                i = 1; letter = C; front = B; back = ''; together = B
                    => B, "CA" length = 1
                        i = 0; letter = B; front = ''; back = ''; together = ''
                            => '', "BCA"
                                => BCA
        i = 1; letter = B; front = A; back = C; together = AC
            => AC; "B" length = 2
                i = 0; letter = A; front = ''; back = C; together = C
                    => C, AB length = 1
                        i = 0; letter = C; front = ''; back = ''; together = ''
                            => '', CAB
                i = 1; letter = C; front = A; back = ''; together = A
                    => A, CB length = 1
                        i = 0; letter = A; front = ''; back = ''; together = '';
                            => '', ACB 
        i = 2; letter = C; front = 'AB'; back = ''; together = AB
            => AB; "C" length = 2
                i = 0; letter = A; front = ''; back = B; together = B
                    => B, "AC" length = 1
                        i = 0; letter = B; front = ''; back = ''; together = ''
                            => '', "BAC"
                                => BAC
                i = 1; letter = B; front = A; back = ''; together = A
                    => A; "BC" length = 1
                        i = 0; letter = A; front = ''; back = ''; together = ''
                            => '', "ABC"
                                => ABC                 
"""