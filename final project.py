#Leah Neufeld
#8176778
#@brocku.ca

import numpy as np
matrix1 = []
matrix2 = []
ciphertext = []
ciphertext1 = []


alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def invmod(x,m):
    for i in range(1, m):
        if x * i %m == 1:
            return(i)
            break

def letter_to_num(L):
    L = L.upper()
    return 0 if L == 'z'else ord(L) - ord('A')+1

def word_to_num(word): 
        return[letter_to_num(L) for L in word.upper()]
    

def matrix_multiply(matrixA,vectorB):
    u = matrixA[0][0]
    v = matrixA[0][1]
    w = matrixA[1][0]
    x = matrixA[1][1]
    
    a = vectorB[0]
    b = vectorB[1]
    
    return[(u*a + v*b)%26, (w*a + x*b)%26]
    
    
def hill_encrypt(phrase, a, b, c, d):
    final_text =""
    num_list = word_to_num(phrase)
    phraselength = len(phrase)
    if phraselength %2== 1:
        num_list.append(num_list[phraselength - 1])
        phraselength+=1
    z=0
    while z < phraselength:
        matrix1.append([num_list[z],num_list[z+1]])
        z+=2
    matrix_key = [[a,b],[c,d]]
    
    for i in range(len(matrix1)):
        ciphertext.append(matrix_multiply(matrix_key,matrix1[i]))
        
    for f in range(len(ciphertext)):
        for g in {0,1}:
            final_text += alphabet[ciphertext[f][g]-1]
        
    return ciphertext, final_text



def inverse_matrix(matrix):
    a = matrix[0][1]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    det_inverse = invmod(a*d - b*c, 26) 
    
    return [[(d*det_inverse)%26, (-b* det_inverse)%26], [(-c*det_inverse)%26, (a*det_inverse)%26]]

def hill_decrypt(phrase, a, b, c, d):
    final_text1=""
    num_list = word_to_num(phrase)
    phraselength = len(phrase)
    z=0
    while z < phraselength:
        matrix2.append([num_list[z],num_list[z+1]])
        z+=2
    matrix_key = [[a,b],[c,d]]
    inverse_matrixkey = inverse_matrix(matrix_key)
    for i in range(len(matrix2)):
        ciphertext1.append (matrix_multiply(inverse_matrixkey,matrix2[i]))
        
    for f in range(len(ciphertext1)):
       for g in {0,1}:
           final_text1 += alphabet[ciphertext1[f][g]-1]
           
    return ciphertext1, final_text1

print(hill_encrypt('IAMHIDING', 1,2,0,3))

print(hill_encrypt('GTNKGKDUSK', 5,6,2,3))
    
        

  


