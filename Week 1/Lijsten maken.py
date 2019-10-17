list = [2,3,4]
list2 = ["red", "green", "blue"]
list3 = range(3,5,1)
list4 = ["a","b","c","d"]

print(list)
print(list2)
print(list3)
print(list4)

L1 = [30,1,2,1,0]
L2 = [1,21,13]

print(L1+L2)
print(3*L2)
print(L1 > L2)
print([x for x in L1])
print([x for x in L1 if x in L2])

String = "Guido van rossum"
print(String.split(" "));

def isPalindroom(str):
    if str[::-1] == str:
        return True
    else:
        return False

print(isPalindroom("lepel"))

seq = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

i = 0
while i < len(seq):
    if seq[i] == "A" and seq[i+1] == "T" and seq[i+2] == "G":
        print(i+3)
    i += 1



