alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
alphabet_inv = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j',
 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x',
  24:'y', 25:'z' }

key = input("What is the key")
encrypted = input("What is it encrypted as")
#omstv
#Hello
#Hi
#HiHiH
#string that says HiHiH from two words
#Hello
#hihih
#mod 26 by 7+7 cuz h+h=14 mod 26
#14 - 7
def decrypt(message, key):
    counter = 0
    new_key = ""
    while (counter < len(message)):
        new_key += key [counter% len(key)] 
        counter+=1
    return new_key
def alph(new_key, message):
    word = ""
    encrypted = message
    for i in range(0, len(encrypted)):
        result = alphabet_pos[new_key[i]] - alphabet_pos[encrypted[i]]
        result = result%26
        word += alphabet_inv[result]
    return word
        #prints letter in key next line alphabet pos takes new key of i goves you a letter new key of i gives a corresponding number with the letter which corresponds to the number where the key is
decrypted = decrypt(encrypted, key)
print (decrypted)
result_word = alph(encrypted, decrypted)
print(result_word)
           
